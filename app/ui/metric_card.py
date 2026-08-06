from app.ui.glass_card import show as glass_card


def show(
    title,
    value,
    subtitle="",
    icon="📊",
):
    glass_card(
        title=title,
        value=value,
        subtitle=subtitle,
        icon=icon,
    )


# Backward compatibility
def metric(
    title,
    value,
    subtitle="",
    icon="📊",
):
    show(
        title=title,
        value=value,
        subtitle=subtitle,
        icon=icon,
    )