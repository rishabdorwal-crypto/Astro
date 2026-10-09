
import math


def dynamic_pressure(rho, velocity):
    """Dynamic pressure, q = 0.5 * rho * V^2, in Pa."""
    return 0.5 * rho * velocity**2


def aerodynamic_coefficients(
    angle_deg,
    cl_alpha_per_rad=2 * math.pi,
    cl_max=1.2,
    stall_angle_deg=14.0,
    cd0=0.025,
    induced_drag_factor=0.06,
):
    """
    Simplified illustrative lift and drag coefficients.

    Assumptions:
    - Linear lift curve before stall.
    - Lift decreases after the assumed stall angle.
    - Drag follows a simple parabolic drag polar.
    - Not validated for a real airfoil or aircraft.
    """
    alpha_rad = math.radians(angle_deg)
    stall_rad = math.radians(stall_angle_deg)

    # Simplified lift curve before stall
    cl_linear = cl_alpha_per_rad * alpha_rad

    # Keep the pre-stall lift coefficient within a simple bound
    cl_pre_stall = max(-cl_max, min(cl_linear, cl_max))

    if abs(angle_deg) <= stall_angle_deg:
        cl = cl_pre_stall
    else:
        # Simplified post-stall behaviour:
        # reduce lift magnitude beyond the assumed stall angle.
        sign = 1 if angle_deg >= 0 else -1
        excess_angle = abs(angle_deg) - stall_angle_deg
        cl_at_stall = min(
            cl_max,
            abs(cl_alpha_per_rad * stall_rad)
        )
        cl = sign * cl_at_stall * math.exp(
            -excess_angle / 12.0
        )

    # Simplified drag polar
    cd = cd0 + induced_drag_factor * cl**2

    # Add extra drag after stall
    if abs(angle_deg) > stall_angle_deg:
        cd += 0.02 * (
            1 - math.exp(
                -(abs(angle_deg) - stall_angle_deg) / 8.0
            )
        )

    return cl, cd


def aerodynamic_forces(
    rho,
    velocity,
    wing_area,
    angle_deg,
    **coefficient_options,
):
    """
    Calculate lift and drag in Newtons.

    Lift = q * S * CL
    Drag = q * S * CD
    """
    q = dynamic_pressure(rho, velocity)

    cl, cd = aerodynamic_coefficients(
        angle_deg, **coefficient_options
    )

    lift = q * wing_area * cl
    drag = q * wing_area * cd

    return {
        "angle_deg": angle_deg,
        "dynamic_pressure_pa": q,
        "CL": cl,
        "CD": cd,
        "lift_N": lift,
        "drag_N": drag,
    }


def stall_speed(
    mass_kg,
    wing_area,
    rho,
    cl_max=1.2,
):
    """
    Idealized stall speed in m/s.

    Vs = sqrt(2 * W / (rho * S * CLmax))

    Assumes level flight and a specified maximum lift coefficient.
    """
    if mass_kg <= 0:
        raise ValueError("Mass must be greater than zero.")
    if wing_area <= 0:
        raise ValueError("Wing area must be greater than zero.")
    if rho <= 0:
        raise ValueError("Air density must be greater than zero.")
    if cl_max <= 0:
        raise ValueError("CLmax must be greater than zero.")

    weight_N = mass_kg * 9.80665

    return math.sqrt(
        (2 * weight_N) / (rho * wing_area * cl_max)
    )


def estimated_wing_root_stress(
    lift_N,
    wingspan_m,
    spar_width_m,
    spar_thickness_m,
):
    """
    Very simplified wing-root bending stress estimate in Pa.

    Assumes:
    - Total lift is distributed symmetrically across both wings.
    - Each half-wing has a uniform lift distribution.
    - A rectangular spar cross-section.
    - The spar behaves as a simple beam.

    This is NOT a structural certification calculation.
    """
    if wingspan_m <= 0:
        raise ValueError("Wingspan must be greater than zero.")
    if spar_width_m <= 0 or spar_thickness_m <= 0:
        raise ValueError("Spar dimensions must be greater than zero.")

    # Root bending moment for uniform lift distribution
    root_moment = abs(lift_N) * wingspan_m / 8.0

    # Second moment of area for rectangular section
    second_moment = (
        spar_width_m * spar_thickness_m**3 / 12.0
    )

    outer_fibre_distance = spar_thickness_m / 2.0

    stress_pa = (
        root_moment * outer_fibre_distance / second_moment
    )

    return {
        "root_moment_Nm": root_moment,
        "stress_Pa": stress_pa,
        "stress_MPa": stress_pa / 1e6,
    }
