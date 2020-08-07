# For more information check Pydantic documentation = https://pydantic-docs.helpmanual.io/usage/models/
#
# Creating your custom classes
#
# class ClassName(BaseModel):
#     name: str
#     value: int
#

from pydantic import BaseModel, Field


class Model(BaseModel):
    pass
