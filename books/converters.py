from datetime import date


class DateConverter:
   regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'

   @staticmethod
   def to_python(value: str) -> date:
       return date.fromisoformat(value)

   @staticmethod
   def to_url(value: date) -> str:
       return value.isoformat()
