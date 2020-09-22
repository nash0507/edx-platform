"""
Toggles for courseware in-course experience.
"""

from lms.djangoapps.experiments.flags import ExperimentWaffleFlag
from openedx.core.djangoapps.waffle_utils import CourseWaffleFlag, WaffleFlagNamespace

# Namespace for courseware waffle flags.
WAFFLE_FLAG_NAMESPACE = WaffleFlagNamespace(name='courseware')

# .. toggle_name: courseware.courseware_mfe
# .. toggle_implementation: ExperimentWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to redirect to another learner profile experience. Supports staged rollout to
#   students for a new micro-frontend-based implementation of the courseware page.
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2020-01-29
# .. toggle_target_removal_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and
#   ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: TNL-7000
REDIRECT_TO_COURSEWARE_MICROFRONTEND = ExperimentWaffleFlag(
    WAFFLE_FLAG_NAMESPACE, 'courseware_mfe', __name__, use_course_aware_bucketing=False
)

# .. toggle_name: courseware.microfrontend_course_team_preview
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Waffle flag to display a link for the new learner experience to course teams without
#   redirecting students. Supports staged rollout to course teams of a new micro-frontend-based implementation of the
#   courseware page.
# .. toggle_use_cases: temporary, open_edx
# .. toggle_creation_date: 2020-03-09
# .. toggle_target_removal_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and
#   ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: TNL-6982
COURSEWARE_MICROFRONTEND_COURSE_TEAM_PREVIEW = CourseWaffleFlag(
    WAFFLE_FLAG_NAMESPACE, 'microfrontend_course_team_preview', __name__
)

# Waffle flag to enable the course end page in the learning MFE.
#
# .. toggle_name: courseware.microfrontend_course_end
# .. toggle_implementation: CourseWaffleFlag
# .. toggle_default: False
# .. toggle_description: Supports staged rollout of the new micro-frontend-based implementation of the course end page.
# .. toggle_category: micro-frontend
# .. toggle_use_cases: incremental_release, open_edx
# .. toggle_creation_date: UPDATE ME BEFORE MERGE
# .. toggle_expiration_date: 2020-12-31
# .. toggle_warnings: Also set settings.LEARNING_MICROFRONTEND_URL and ENABLE_COURSEWARE_MICROFRONTEND.
# .. toggle_tickets: AA-188
COURSEWARE_MICROFRONTEND_COURSE_END = CourseWaffleFlag(
    WAFFLE_FLAG_NAMESPACE, 'microfrontend_course_end', __name__
)


def course_end_is_active(course_key):
    return (
        REDIRECT_TO_COURSEWARE_MICROFRONTEND.is_enabled(course_key) and
        COURSEWARE_MICROFRONTEND_COURSE_END.is_enabled(course_key)
    )
