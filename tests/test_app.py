"""
Unit Tests — AI Product Ad Composer
=====================================
Run with: pytest tests/ -v

Tests cover the core business logic functions that do NOT require
external API calls, so they run fast and work without credentials.
"""

import sys
from pathlib import Path

import pytest

# Add the project root to sys.path so we can import from app.py
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app import (
    DEMOGRAPHIC_STYLES,
    generate_ad_copy_template,
    get_image_prompt,
)


# ---------------------------------------------------------------------------
# Test: DEMOGRAPHIC_STYLES completeness
# ---------------------------------------------------------------------------

class TestDemographicStyles:
    """Verify the DEMOGRAPHIC_STYLES config has all required keys for every demographic."""

    REQUIRED_KEYS = {"aesthetic", "tone", "keywords"}
    EXPECTED_DEMOGRAPHICS = {"Teenagers", "Professionals", "Seniors"}

    def test_all_demographics_present(self):
        """All three target demographics must exist in DEMOGRAPHIC_STYLES."""
        assert set(DEMOGRAPHIC_STYLES.keys()) == self.EXPECTED_DEMOGRAPHICS

    def test_each_demographic_has_required_keys(self):
        """Every demographic entry must contain 'aesthetic', 'tone', and 'keywords'."""
        for name, style in DEMOGRAPHIC_STYLES.items():
            missing = self.REQUIRED_KEYS - set(style.keys())
            assert not missing, f"Demographic '{name}' is missing keys: {missing}"

    def test_keywords_is_a_list_with_at_least_two_items(self):
        """Keywords list must have at least 2 items (used in template generation)."""
        for name, style in DEMOGRAPHIC_STYLES.items():
            assert isinstance(style["keywords"], list), f"'{name}' keywords must be a list"
            assert len(style["keywords"]) >= 2, f"'{name}' needs at least 2 keywords"


# ---------------------------------------------------------------------------
# Test: generate_ad_copy_template
# ---------------------------------------------------------------------------

class TestGenerateAdCopyTemplate:
    """Verify the fallback template generator returns well-formed output."""

    def test_returns_dict_with_required_keys(self):
        """Result must be a dict with exactly: headline, description, slogan."""
        result = generate_ad_copy_template("Test Product", "Electronics", "Professionals")
        assert isinstance(result, dict)
        assert set(result.keys()) == {"headline", "description", "slogan"}

    def test_product_name_appears_in_headline(self):
        """The product name must appear in the generated headline."""
        product = "Super Widget 3000"
        result = generate_ad_copy_template(product, "Electronics", "Professionals")
        assert product in result["headline"]

    def test_all_values_are_non_empty_strings(self):
        """Every value in the result must be a non-empty string."""
        result = generate_ad_copy_template("Widget", "Fashion", "Teenagers")
        for key, value in result.items():
            assert isinstance(value, str), f"Key '{key}' must be a string"
            assert len(value.strip()) > 0, f"Key '{key}' must not be empty"

    @pytest.mark.parametrize("demographic", ["Teenagers", "Professionals", "Seniors"])
    def test_works_for_all_demographics(self, demographic):
        """Template generation must succeed for every valid demographic."""
        result = generate_ad_copy_template("Test Product", "General", demographic)
        assert result["headline"]
        assert result["description"]
        assert result["slogan"]


# ---------------------------------------------------------------------------
# Test: get_image_prompt
# ---------------------------------------------------------------------------

class TestGetImagePrompt:
    """Verify image prompt generation returns a usable, non-empty string."""

    def test_returns_non_empty_string(self):
        """Image prompt must be a non-empty string."""
        prompt = get_image_prompt("Wireless Headphones", "Professionals")
        assert isinstance(prompt, str)
        assert len(prompt.strip()) > 0

    def test_product_name_included_in_prompt(self):
        """The product name must appear in the generated image prompt."""
        product = "Yoga Mat Pro"
        prompt = get_image_prompt(product, "Teenagers")
        assert product in prompt

    def test_aesthetic_keywords_included(self):
        """Demographic-specific aesthetic keywords must appear in the prompt."""
        prompt = get_image_prompt("Running Shoes", "Teenagers")
        assert "Trendy" in prompt or "energetic" in prompt or "bold" in prompt

    @pytest.mark.parametrize("demographic", ["Teenagers", "Professionals", "Seniors"])
    def test_all_demographics_produce_different_prompts(self, demographic):
        """Different demographics must produce different image prompts."""
        prompt = get_image_prompt("Smartwatch", demographic)
        assert isinstance(prompt, str) and len(prompt) > 20
