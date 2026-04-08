import os
from zipfile import ZipFile

# Файловая структура под XenForo
os.makedirs("upload/styles/ArizonaRP", exist_ok=True)
os.makedirs("upload/styles/ArizonaRP/xenforo", exist_ok=True)
os.makedirs("upload/styles/ArizonaRP/images", exist_ok=True)
os.makedirs("upload/styles/ArizonaRP/css", exist_ok=True)

# --- style.xml ---
style_xml = """<?xml version="1.0" encoding="utf-8"?>
<style title="Arizona RP Full Style" version_id="100" version_string="1.0">
    <properties>
        <property name="arizona_primary_color">#c0392b</property>
        <property name="arizona_secondary_color">#8e44ad</property>
        <property name="background_image">@styles/ArizonaRP/images/black_russia_bg.jpg</property>
    </properties>

    <templates>
        <template name="PAGE_CONTAINER">
<![CDATA[
<div class="arizona-wrapper">
    <div class="arizona-bg"></div>
    <div class="arizona-content">
        <xen:include template="header" />
        <xen:contents />
        <xen:include template="footer" />
    </div>
</div>
]]>
        </template>

        <template name="header">
<![CDATA[
<header class="arizona-header">
    <h1>Arizona RolePlay</h1>
</header>
]]>
        </template>

        <template name="footer">
<![CDATA[
<footer class="arizona-footer">
    <span>© Arizona RP — Custom XenForo Style</span>
</footer>
]]>
        </template>

    </templates>
</style>
"""

with open("style.xml", "w", encoding="utf-8") as f:
    f.write(style_xml)


# --- CSS ---
css_content = """
.arizona-wrapper {
    position: relative;
    min-height: 100vh;
}
.arizona-bg {
    background: url('../images/black_russia_bg.jpg') center/cover no-repeat fixed;
    position: absolute;
    inset: 0;
    z-index: -1;
    opacity: 0.8;
}
.arizona-header {
    background: rgba(192, 57, 43, 0.9);
    padding: 20px;
    color: white;
    text-align: center;
    font-size: 32px;
}
.arizona-footer {
    text-align: center;
    padding: 20px;
    background: rgba(0,0,0,0.6);
    color: white;
}
"""

with open("upload/styles/ArizonaRP/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)


# --- Заглушка изображения ---
with open("upload/styles/ArizonaRP/images/black_russia_bg.jpg", "wb") as f:
    f.write(b"\x00")  # Заглушка, заменишь позже


# --- Создание ZIP ---
zip_name = "ArizonaRP_full_style.zip"

with ZipFile(zip_name, "w") as zipf:
    zipf.write("style.xml")
    for root, dirs, files in os.walk("upload"):
        for file in files:
            filepath = os.path.join(root, file)
            zipf.write(filepath)

print("Готово! Файл ArizonaRP_full_style.zip создан.")
