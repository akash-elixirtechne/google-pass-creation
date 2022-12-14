import os
import uuid

from Google_pass_api import DemoGeneric

demo = DemoGeneric()

issuer_id = "3388000000022190363"

auth_response = demo.auth()

generic_class = demo.create_class(
    issuer_id=issuer_id,
    class_suffix=uuid.uuid4().hex
)
print(generic_class)

class_suffix = generic_class.split(".")[-1]

create_object_with_download_pass = demo.create_jwt_new_objects(
    issuer_id=issuer_id,
    class_suffix=class_suffix,
    object_suffix=uuid.uuid4().hex
)


print(create_object_with_download_pass)