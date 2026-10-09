
import math


def validate_inputs(
    rho,
    velocity,
    wing_area,
    mass_kg,
    angle_deg,
    cl_max,
    stall_angle_deg,
):
    """Return a list of input errors and engineering warnings."""

    errors = []
    warnings = []

    if not math.isfinite(rho) or rho <= 0:
        errors.append("Air density must be a finite positive value.")

    if not math.isfinite(velocity) or velocity <= 0:
        errors.append("Air velocity must be a finite positive value.")

    if not math.isfinite(wing_area) or wing_area <= 0:
        errors.append("Wing area must be a finite positive value.")

    if not math.isfinite(mass_kg) or mass_kg <= 0:
        errors.append("Mass must be a finite positive value.")

    if not math.isfinite(cl_max) or cl_max <= 0:
        errors.append("Maximum lift coefficient must be positive.")

    if not math.isfinite(stall_angle_deg) or stall_angle_deg <= 0:
        errors.append("Assumed stall angle must be positive.")

    if not math.isfinite(angle_deg):
        errors.append("Angle of attack must be a finite number.")
    elif abs(angle_deg) > 20:
        warnings.append(
            "Angle is outside the dashboard's recommended "
            "illustrative range of -20 to +20 degrees."
        )

    if (
        math.isfinite(angle_deg)
        and math.isfinite(stall_angle_deg)
        and stall_angle_deg > 0
        and abs(angle_deg) >= stall_angle_deg
    ):
        warnings.append(
            "The model is at or beyond its assumed stall angle. "
            "Post-stall estimates are highly simplified."
        )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


def validate_result(result):
    """Check that calculated numeric outputs are finite."""

    errors = []

    for name, value in result.items():
        if isinstance(value, (int, float)):
            if not math.isfinite(value):
                errors.append(
                    f"{name} is not a finite numeric result."
                )

    return {
        "valid": len(errors) == 0,
        "errors": errors,
    }


def data_status(source):
    """Make the origin of data explicit."""

    if source == "simulation":
        return (
            "SIMULATED DATA — illustrative only; "
            "not measured by physical sensors."
        )

    if source == "measured":
        return (
            "USER-ENTERED MEASUREMENTS — verify sensor calibration "
            "and measurement uncertainty."
        )

    return "UNKNOWN DATA SOURCE — do not treat as validated results."
