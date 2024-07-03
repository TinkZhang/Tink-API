from flask_restx import Api

from apis.bus.bus_api import api as ns_bus

api = Api(
    title='Tink\'s API',
    version='1.0',
    description='These APIs are designed for my hobby projects',
    # All API metadatas
)

api.add_namespace(ns_bus)
