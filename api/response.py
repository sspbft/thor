from flask import jsonify

class Response:
  """Models an HTTP response"""

  def __init__(self, code=200, data={}):
    self.code = code
    self.data = data

  def as_json(self):
    return jsonify({
      "code": self.code,
      "data": self.data
    })