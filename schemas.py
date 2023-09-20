from marshmallow import Schema, fields, validates_schema, ValidationError


class RequestParamsSchema(Schema):
    cmd = fields.Str(required=True)
    value = fields.Str(required=True)



    @validates_schema
    def validate_cmd_param(self, values, *args, **kwargs):
        valid_cmd_commands = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_commands:
            raise ValidationError({'cmd':f'contains invalid command={values["cmd"]}'})

        return values


class RequestParamsListSchema(Schema):
    queries = fields.Nested(RequestParamsSchema, many=True)
    file_name = fields.Str(required=True)