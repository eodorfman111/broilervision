"""BroilerVision config — reference implementation of the cv_demo_engine template.

Live demo runs zero-shot on the coop-floor clip (bright/sharp enough that no
fine-tuning was needed). A custom-trained model also exists for barn-style
hazy footage (broilervision_best.pt, class 0 = Chicken) — see
project_broilervision memory for why the two clips needed different approaches.
"""
from pathlib import Path
from cv_demo_engine.config_schema import Config, ImpactStat, CapabilityCard

CONFIG = Config(
    slug="broilervision",
    industry_name="BroilerVision",
    icon_emoji="🐔",
    accent_hex="#38bdf8",
    base_dir=Path(__file__).parent,

    # Footage / model
    boxes_source_clip="coop_source.mp4",
    alerts_source_clip="coop_alerts_source.mp4",  # staged: downed bird + huddle cluster
    loop_count=4,
    model_path="yolo26n.pt",
    target_class_id=14,             # COCO "bird" — zero-shot, no fine-tuning needed on this clip
    target_class_name="Chicken",
    is_custom_trained=False,
    conf=0.20,
    imgsz=1920,
    max_det=2000,

    # Calibrated against coop_alerts_source.mp4 (see cv_demo_engine.calibrate output)
    stress_thresh=9.021,
    crowd_thresh=0.263,
    mortality_move_px=12,
    # This clip is staged with exactly one downed bird — cap display to the
    # single longest-standing alert so a briefly-paused feeding bird never
    # draws a second marker. A real deployment should raise this.
    max_simultaneous_mortality_alerts=1,

    # Hero copy
    hero_badge="BroilerVision · AI Overhead Monitoring",
    hero_headline="See every bird in the house, every second — not just on walk-throughs",
    hero_subheadline=(
        "Live bird counts, early crowding alerts, and same-day mortality detection — "
        "problems your team would otherwise catch a day or two late."
    ),

    # Impact strip — the ROI pitch
    impact_stats=[
        ImpactStat("60&ndash;70%", "of production cost is feed"),
        ImpactStat("$1,000s", "saved per FCR point, per 20k-bird house"),
        ImpactStat("42&ndash;49 days", "grow-out cycle length"),
    ],

    # Capability cards
    capability_cards=[
        CapabilityCard("🎯", "Per-Site Model Tuning", "roadmap",
            "Bright, high-contrast houses run well off-the-shelf, like this one. Hazy, "
            "low-light, or dense litter-floor housing gets a <b>custom fine-tune</b> on "
            "that site's own footage — already validated on a separate barn clip."),
        CapabilityCard("🔢", "Live Bird Counting &amp; Density", "live",
            "Frame-by-frame flock counts with per-track identity — the first input "
            "for <b>FCR tracking</b> (feed intake ÷ population)."),
        CapabilityCard("🌡️", "Crowding &amp; Cold-Spot Detection", "live",
            "Spatial clustering flags huddling patterns before they show up as uneven "
            "weight gain — often the earliest visible sign of a <b>ventilation fault</b>."),
        CapabilityCard("⚠️", "Mortality Watch", "live",
            "Per-track immobility detection flags a downed bird the same day, instead "
            "of waiting on the next <b>manual walk-through</b>."),
        CapabilityCard("🏭", "Fleet-Wide Rollup", "roadmap",
            "One dashboard across every contract house in the complex — spot the "
            "<b>3 houses dragging down</b> your average FCR before the flock closes out."),
        CapabilityCard("⚖️", "Weight &amp; Uniformity Estimation", "roadmap",
            "Pixel-area-to-weight modeling tracks flock <b>uniformity drift</b> — "
            "a leading indicator of FCR problems weeks before scale-out weights confirm it."),
        CapabilityCard("🦵", "Gait &amp; Lameness Scoring", "roadmap",
            "Locomotion tracking flags early leg-health issues continuously — the same "
            "welfare metric <b>EU auditors score by hand</b> once a cycle."),
        CapabilityCard("📲", "Instant Alerts", "roadmap",
            "Mortality spikes and crowding events push straight to a phone or Slack "
            "channel — <b>no one has to be watching</b> a dashboard for it to catch a problem."),
        CapabilityCard("📈", "FCR Impact", "live",
            "Feed is <b>60&ndash;70% of production cost</b>. A single FCR point saved "
            "across a 20k-bird house is worth thousands per cycle — count and behavior "
            "data is the input this pitch runs on."),
        CapabilityCard("🎥", "Deploys On Existing Cameras", "live",
            "PoE/Cat6 architecture, IP66+ enclosures, 940nm IR for post-transfer "
            "low-light housing — no rip-and-replace of barn infrastructure."),
    ],

    # Video captions — two distinct capabilities, not the same clip twice
    alerts_video_label="🚨 MORTALITY &amp; CROWDING ALERTS",
    alerts_video_caption=(
        "Pulsing marker on any bird flagged by Mortality Watch, highlighted zone when "
        "crowding triggers — the alert system in action, not just a detection count."
    ),
    boxes_video_label="📦 DETECTION BOXES — PER-BIRD CONFIDENCE",
    boxes_video_caption=(
        "Every visible bird detected and confidence-scored, frame by frame. Hazier, "
        "lower-light houses get a model fine-tuned on that site's own footage — "
        "ask about the barn-lighting variant."
    ),

    # CTA
    cta_headline="Want to see this running on your own barn footage?",
    cta_body=(
        "Send a clip from one house and I'll turn around a version like this one — "
        "count, crowding, and mortality watch tuned to your camera and lighting."
    ),
)
