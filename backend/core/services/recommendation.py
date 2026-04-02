import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from core.models import Enrollment, Course


def get_course_recommendations(user_id, top_n=5):
    """
    Returns list of recommended course IDs
    """

    enrollments = Enrollment.objects.all().values('user_id', 'course_id')

    if not enrollments:
        return []

    df = pd.DataFrame(enrollments)

    if df.empty:
        return []

    # Create user-course matrix
    user_course_matrix = pd.crosstab(df['user_id'], df['course_id'])

    # If user not in matrix
    if user_id not in user_course_matrix.index:
        return []

    # Compute similarity
    similarity_matrix = cosine_similarity(user_course_matrix)

    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=user_course_matrix.index,
        columns=user_course_matrix.index
    )

    # Get similar users
    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:6]

    user_courses = set(df[df['user_id'] == user_id]['course_id'])

    recommended_courses = set()

    for sim_user_id in similar_users.index:
        sim_user_courses = set(
            df[df['user_id'] == sim_user_id]['course_id']
        )

        recommended_courses.update(sim_user_courses - user_courses)

    return list(recommended_courses)[:top_n]


def get_course_recommendations_with_objects(user_id, top_n=5):
    """
    Returns actual Course queryset
    """
    course_ids = get_course_recommendations(user_id, top_n)

    if not course_ids:
        return Course.objects.none()

    return Course.objects.filter(id__in=course_ids)