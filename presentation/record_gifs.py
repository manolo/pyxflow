"""
Record animated GIFs from the PyFlow demo app.

Usage:
    python presentation/record_gifs.py          # all demos
    python presentation/record_gifs.py hello     # just hello world
    python presentation/record_gifs.py grid      # just grid

Requires: playwright, ffmpeg
Server must be running on :8089
"""
import subprocess
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_URL = "http://localhost:8089"
OUT_DIR = Path(__file__).parent / "images"
VIDEO_DIR = Path(__file__).parent / "videos_tmp"


def wait_for_vaadin(page, timeout=10000):
    """Wait until Vaadin client is fully loaded and idle."""
    page.wait_for_function(
        """() => {
            const client = window.Vaadin && window.Vaadin.Flow &&
                           window.Vaadin.Flow.clients &&
                           Object.values(window.Vaadin.Flow.clients)[0];
            return client && !client.isActive();
        }""",
        timeout=timeout,
    )
    page.wait_for_timeout(300)


def to_gif(video_path: Path, gif_path: Path, fps=12, width=800):
    """Convert webm video to optimized GIF using ffmpeg."""
    # Two-pass for better quality: generate palette first, then use it
    palette = video_path.with_suffix(".png")
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path),
        "-vf", f"fps={fps},scale={width}:-1:flags=lanczos,palettegen=stats_mode=diff",
        str(palette),
    ], capture_output=True)
    subprocess.run([
        "ffmpeg", "-y", "-i", str(video_path), "-i", str(palette),
        "-lavfi", f"fps={fps},scale={width}:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer:bayer_scale=3",
        str(gif_path),
    ], capture_output=True)
    palette.unlink(missing_ok=True)
    print(f"  -> {gif_path} ({gif_path.stat().st_size // 1024} KB)")


def record_hello(browser):
    """Hello World: type name, click button, notification appears."""
    print("Recording: Hello World")
    ctx = browser.new_context(
        viewport={"width": 900, "height": 600},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 900, "height": 600},
    )
    page = ctx.new_page()
    page.goto(f"{BASE_URL}/hello")
    wait_for_vaadin(page)
    page.wait_for_timeout(800)

    # Find the text field and type slowly
    tf = page.locator("vaadin-text-field")
    tf.click()
    page.wait_for_timeout(300)
    for ch in "Manolo":
        page.keyboard.type(ch, delay=80)
        page.wait_for_timeout(50)
    page.wait_for_timeout(500)

    # Click the button
    btn = page.locator("vaadin-button", has_text="Say hello")
    btn.click()
    page.wait_for_timeout(2000)  # wait for notification to show & linger

    # Close
    ctx.close()
    video = list(VIDEO_DIR.glob("*.webm"))[-1]
    to_gif(video, OUT_DIR / "demo-hello.gif", fps=12, width=800)


def record_components(browser):
    """Components: close drawer, scroll slowly to bottom."""
    print("Recording: Components")
    ctx = browser.new_context(
        viewport={"width": 1100, "height": 700},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1100, "height": 700},
    )
    page = ctx.new_page()
    page.goto(f"{BASE_URL}/components")
    wait_for_vaadin(page)
    page.wait_for_timeout(1000)

    # Close the drawer by clicking the menu toggle (hamburger)
    toggle = page.locator("vaadin-drawer-toggle")
    if toggle.count() > 0:
        toggle.click()
        page.wait_for_timeout(600)

    # Scroll slowly — find the main scrollable area
    # The content is in the app-layout's content slot
    content = page.locator("[slot=''] vaadin-vertical-layout, vaadin-vertical-layout").first
    if content.count() == 0:
        content = page.locator("#outlet").first

    # Smooth scroll using JS
    page.evaluate("""
        async () => {
            // Find the scrollable container
            const appLayout = document.querySelector('vaadin-app-layout');
            const scrollTarget = appLayout
                ? (appLayout.shadowRoot.querySelector('[part="content"]') || appLayout)
                : document.documentElement;
            const totalHeight = scrollTarget.scrollHeight - scrollTarget.clientHeight;
            const duration = 4000;
            const start = performance.now();
            return new Promise(resolve => {
                function step(timestamp) {
                    const progress = Math.min((timestamp - start) / duration, 1);
                    // ease in-out
                    const ease = progress < 0.5
                        ? 2 * progress * progress
                        : -1 + (4 - 2 * progress) * progress;
                    scrollTarget.scrollTop = ease * totalHeight;
                    if (progress < 1) requestAnimationFrame(step);
                    else resolve();
                }
                requestAnimationFrame(step);
            });
        }
    """)
    page.wait_for_timeout(500)

    ctx.close()
    video = list(VIDEO_DIR.glob("*.webm"))[-1]
    to_gif(video, OUT_DIR / "demo-components.gif", fps=10, width=900)


def record_grid(browser):
    """Grid: scroll slowly to the bottom."""
    print("Recording: Grid")
    ctx = browser.new_context(
        viewport={"width": 1000, "height": 650},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1000, "height": 650},
    )
    page = ctx.new_page()
    page.goto(f"{BASE_URL}/grid")
    wait_for_vaadin(page)
    page.wait_for_timeout(1000)

    # Scroll the grid slowly using its internal scroller
    page.evaluate("""
        async () => {
            const grid = document.querySelector('vaadin-grid');
            const scroller = grid.shadowRoot.querySelector('#table');
            const totalHeight = scroller.scrollHeight - scroller.clientHeight;
            const duration = 5000;
            const start = performance.now();
            return new Promise(resolve => {
                function step(timestamp) {
                    const progress = Math.min((timestamp - start) / duration, 1);
                    const ease = progress < 0.5
                        ? 2 * progress * progress
                        : -1 + (4 - 2 * progress) * progress;
                    scroller.scrollTop = ease * totalHeight;
                    if (progress < 1) requestAnimationFrame(step);
                    else resolve();
                }
                requestAnimationFrame(step);
            });
        }
    """)
    page.wait_for_timeout(500)

    ctx.close()
    video = list(VIDEO_DIR.glob("*.webm"))[-1]
    to_gif(video, OUT_DIR / "demo-grid.gif", fps=10, width=800)


def record_master_detail(browser):
    """Master-Detail: select row, edit fields, save."""
    print("Recording: Master-Detail")
    ctx = browser.new_context(
        viewport={"width": 1100, "height": 700},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 1100, "height": 700},
    )
    page = ctx.new_page()
    page.goto(f"{BASE_URL}/master-detail")
    wait_for_vaadin(page)
    page.wait_for_timeout(1000)

    # Click on a row in the grid (3rd row for variety)
    grid = page.locator("vaadin-grid")
    # Click on a cell in the grid to select a row
    cells = page.locator("vaadin-grid-cell-content")
    # Find a visible cell with content (skip headers)
    # Click the 3rd data row (roughly index 6 if 2 header cells + 2 cols per row)
    grid.evaluate("""
        el => {
            const rows = el._getRenderedRows();
            if (rows.length > 2) rows[2].click();
        }
    """)
    page.wait_for_timeout(800)
    wait_for_vaadin(page)

    # Edit First Name
    first_name = page.locator("vaadin-text-field").first
    first_name.click()
    page.wait_for_timeout(200)
    page.keyboard.press("Meta+a")
    page.wait_for_timeout(100)
    for ch in "Carlos":
        page.keyboard.type(ch, delay=60)
    page.wait_for_timeout(300)
    page.keyboard.press("Tab")
    page.wait_for_timeout(300)

    # Edit Last Name (next text field)
    page.keyboard.press("Meta+a")
    page.wait_for_timeout(100)
    for ch in "Garcia":
        page.keyboard.type(ch, delay=60)
    page.wait_for_timeout(300)
    page.keyboard.press("Tab")
    page.wait_for_timeout(300)

    # Edit Date of Birth — type into the date picker
    date_picker = page.locator("vaadin-date-picker")
    if date_picker.count() > 0:
        date_picker.click()
        page.wait_for_timeout(200)
        page.keyboard.press("Meta+a")
        for ch in "1985-03-15":
            page.keyboard.type(ch, delay=40)
        page.wait_for_timeout(200)
        page.keyboard.press("Escape")
        page.wait_for_timeout(300)

    # Toggle "Important" checkbox if present
    checkbox = page.locator("vaadin-checkbox")
    if checkbox.count() > 0:
        checkbox.first.click()
        page.wait_for_timeout(400)

    # Change Role if combo-box present
    combo = page.locator("vaadin-combo-box")
    if combo.count() > 0:
        combo.first.click()
        page.wait_for_timeout(300)
        # Select a different option
        page.keyboard.press("ArrowDown")
        page.wait_for_timeout(150)
        page.keyboard.press("ArrowDown")
        page.wait_for_timeout(150)
        page.keyboard.press("Enter")
        page.wait_for_timeout(400)

    # Click Save
    save_btn = page.locator("vaadin-button", has_text="Save")
    if save_btn.count() > 0:
        save_btn.click()
        page.wait_for_timeout(1500)

    ctx.close()
    video = list(VIDEO_DIR.glob("*.webm"))[-1]
    to_gif(video, OUT_DIR / "demo-master-detail.gif", fps=12, width=900)


def record_push(browser):
    """Push/Stopwatch: click Start, wait 3 seconds, click Stop."""
    print("Recording: Stopwatch")
    ctx = browser.new_context(
        viewport={"width": 900, "height": 600},
        record_video_dir=str(VIDEO_DIR),
        record_video_size={"width": 900, "height": 600},
    )
    page = ctx.new_page()
    page.goto(f"{BASE_URL}/push-demo")
    wait_for_vaadin(page)
    page.wait_for_timeout(800)

    # Click Start/Play
    start_btn = page.locator("vaadin-button", has_text="Start")
    if start_btn.count() == 0:
        start_btn = page.locator("vaadin-button").first
    start_btn.click()
    page.wait_for_timeout(3500)  # watch it count

    # Click Stop
    stop_btn = page.locator("vaadin-button", has_text="Stop")
    if stop_btn.count() == 0:
        stop_btn = page.locator("vaadin-button").nth(1)
    stop_btn.click()
    page.wait_for_timeout(1000)

    ctx.close()
    video = list(VIDEO_DIR.glob("*.webm"))[-1]
    to_gif(video, OUT_DIR / "demo-stopwatch.gif", fps=10, width=800)


RECORDINGS = {
    "hello": record_hello,
    "components": record_components,
    "grid": record_grid,
    "master-detail": record_master_detail,
    "push": record_push,
}


def main():
    VIDEO_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)

    targets = sys.argv[1:] if len(sys.argv) > 1 else list(RECORDINGS.keys())

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for name in targets:
            if name in RECORDINGS:
                try:
                    RECORDINGS[name](browser)
                except Exception as e:
                    print(f"  ERROR recording {name}: {e}")
            else:
                print(f"  Unknown target: {name}")
        browser.close()

    # Cleanup temp videos
    for f in VIDEO_DIR.glob("*.webm"):
        f.unlink()
    if VIDEO_DIR.exists() and not list(VIDEO_DIR.iterdir()):
        VIDEO_DIR.rmdir()

    print("\nDone! GIFs saved in presentation/images/")


if __name__ == "__main__":
    main()
