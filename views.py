from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from schemas import RequestParamsSchema
from utils import build_query

main_bp = Blueprint('main', __name__)


@main_bp.route('/unique_query', methods=['POST'])
def perform_query():
    try:
        params = RequestParamsSchema.load(request.json)
    except ValidationError as error:
        return error.messages,'400'

    result = None
    for query in params['queries']:
        result = build_query(
            cmd=query['cmd'],
            param=query['value'],
            file_name=params['file_name'],
            data=result
        )

    return jsonify(result), '200'

