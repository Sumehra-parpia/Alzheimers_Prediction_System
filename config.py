import streamlit as st

# PAGE CONFIG
CSS = open("assets/css/styles.css", 'r').read()

# ASSETS
BACKGROUND = "assets/images/bg.webp"
BANNER = "assets/images/banner.webp"
DEFAULT_IMAGE = "assets/images/default.webp"
SIDE_BANNER = "assets/images/side_banner.webp"
EMOJI = "assets/images/emo.webp"

# PREDICTION PAGE
APOE_CATEGORIES = []
PTHETHCAT_CATEGORIES = []
IMPUTED_CATEGORIES = []
PTRACCAT_CATEGORIES = []
PTGENDER_CATEGORIES = []
APOE4_CATEGORIES = []

ABBREVIATION = {
    "AD": "Alzheimer's Disease",
    "LMCI": "Late Mild Cognitive Impairment",
    "CN": "Cognitively Normal"
}

CONDITION_DESCRIPTION = {
    "AD": "Alzheimer's disease is a progressive brain disorder affecting memory.",
    "LMCI": "Late Mild Cognitive Impairment is an early stage of memory loss.",
    "CN": "Cognitively Normal indicates no major memory issues."
}

# DISABLE SECRETS COMPLETELY
NEWS_API_KEY = ""
KEYWORD = "alzheimer"

HF_EMAIL = ""
HF_PASS = ""
BASE_PROMPT = "You are a helpful assistant."

TEAM_MEMBERS = []
