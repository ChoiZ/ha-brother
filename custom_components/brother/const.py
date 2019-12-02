"""Constants for Brother integration."""
ATTR_BELT_UNIT_REMAINING_LIFE = "belt_unit_remaining_life"
ATTR_BLACK_TONER = "black_toner"
ATTR_BLACK_TONER_REMAINING = "black_toner_remaining"
ATTR_CYAN_TONER = "cyan_toner"
ATTR_CYAN_TONER_REMAINING = "cyan_toner_remaining"
ATTR_DRUM_COUNTER = "drum_counter"
ATTR_DRUM_REMAINING_LIFE = "drum_remaining_life"
ATTR_DRUM_REMAINING_PAGES = "drum_remaining_pages"
ATTR_FUSER_REMAINING_LIFE = "fuser_remaining_life"
ATTR_ICON = "icon"
ATTR_LABEL = "label"
ATTR_LASER_REMAINING_LIFE = "laser_remaining_life"
ATTR_MAGENTA_TONER = "magenta_toner"
ATTR_MAGENTA_TONER_REMAINING = "magenta_toner_remaining"
ATTR_PF_KIT_1_REMAINING_LIFE = "pf_kit_1_remaining_life"
ATTR_PF_KIT_MP_REMAINING_LIFE = "pf_kit_mp_remaining_life"
ATTR_PRINTER_COUNTER = "printer_counter"
ATTR_STATUS = "status"
ATTR_UNIT = "unit"
ATTR_YELLOW_TONER = "yellow_toner"
ATTR_YELLOW_TONER_REMAINING = "yellow_toner_remaining"

DEFAULT_NAME = "Brother Printer"
DOMAIN = "brother"

UNIT_PERCENT = "%"
UNIT_PAGES = "p"

SENSOR_TYPES = {
    ATTR_STATUS: {
        ATTR_ICON: "icon:mdi:printer",
        ATTR_LABEL: ATTR_STATUS.replace("_", " ").title(),
        ATTR_UNIT: None,
    },
    ATTR_PRINTER_COUNTER: {
        ATTR_ICON: "mdi:file-document-outline",
        ATTR_LABEL: ATTR_PRINTER_COUNTER.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PAGES,
    },
    ATTR_DRUM_REMAINING_LIFE: {
        ATTR_ICON: "mdi:chart-donut",
        ATTR_LABEL: ATTR_DRUM_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_BELT_UNIT_REMAINING_LIFE: {
        ATTR_ICON: "mdi:current-ac",
        ATTR_LABEL: ATTR_BELT_UNIT_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_FUSER_REMAINING_LIFE: {
        ATTR_ICON: "mdi:water-outline",
        ATTR_LABEL: ATTR_FUSER_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_LASER_REMAINING_LIFE: {
        ATTR_ICON: "mdi:spotlight-beam",
        ATTR_LABEL: ATTR_LASER_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_PF_KIT_1_REMAINING_LIFE: {
        ATTR_ICON: "mdi:printer-3d",
        ATTR_LABEL: ATTR_PF_KIT_1_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_PF_KIT_MP_REMAINING_LIFE: {
        ATTR_ICON: "mdi:printer-3d",
        ATTR_LABEL: ATTR_PF_KIT_MP_REMAINING_LIFE.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_BLACK_TONER: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_BLACK_TONER.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_BLACK_TONER_REMAINING: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_BLACK_TONER_REMAINING.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_CYAN_TONER: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_CYAN_TONER.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_CYAN_TONER_REMAINING: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_CYAN_TONER_REMAINING.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_MAGENTA_TONER: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_MAGENTA_TONER.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_MAGENTA_TONER_REMAINING: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_MAGENTA_TONER_REMAINING.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_YELLOW_TONER: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_YELLOW_TONER.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
    ATTR_YELLOW_TONER_REMAINING: {
        ATTR_ICON: "mdi:printer-3d-nozzle-outline",
        ATTR_LABEL: ATTR_YELLOW_TONER_REMAINING.replace("_", " ").title(),
        ATTR_UNIT: UNIT_PERCENT,
    },
}
