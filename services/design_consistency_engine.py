import re


def apply_design_consistency(html, palette, font):

    # Replace font-family
    html = re.sub(
        r"font-family:[^;]+;",
        f"font-family:{font['name']};",
        html
    )

    # Replace primary colors
    html = re.sub(
        r"#[0-9a-fA-F]{6}",
        palette["primary_color"],
        html
    )

    # Normalize container width
    html = html.replace(
        "container",
        "container standardized-container"
    )

    return html