from flask_restx import Api

from apis.bus.bus_api import api as ns_bus
from apis.shaokang.shaokang_api import api as ns_sk

api = Api(
    title='Tink\'s API',
    version='1.0',
    description='These APIs are designed for my hobby projects',
    # All API metadatas
)

api.add_namespace(ns_bus)
api.add_namespace(ns_sk)