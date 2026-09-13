"""Constants for the HA CI Demo integration."""

DOMAIN = "ha_ci_demo"
# No platform modules in this demo. A name here with no matching module blocks every
# PR via check_platforms_have_modules, which left the testbed unable to land a sync;
# that check's failing path is covered by test_platforms_naming_a_missing_module_fails.
PLATFORMS: list[str] = []
