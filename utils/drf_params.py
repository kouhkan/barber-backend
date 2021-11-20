from drf_yasg import openapi


# adds jwt header field to swagger-ui
jwt_key = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    description="jwt token",
    type=openapi.TYPE_STRING,
    required=True,
    default="Bearer access_token",
)
