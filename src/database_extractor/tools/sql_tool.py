# from typing import Type
from typing import Union
from crewai.tools import BaseTool
from pydantic import Field
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text


class CustomSQLTool(BaseTool):
    name: str = "CustomSQLTool"
    description: str = "Converts natural language to SQL queries and executes them for SQL Server Database."
    db_uri: str = Field(
        title="Database URL",
        description="The URL of the database to connect to.",
    )

    def _run(self, sql_query: str):
        try:
            data = self.execute_sql(sql_query)
        except Exception as exc:
            data = (
                f"Get the original request {sql_query} and the error {exc} and create the correct SQL query."
            )

        return data

    def execute_sql(self, sql_query: str) -> Union[list, str]:
        engine = create_engine(self.db_uri)
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            result = session.execute(text(sql_query))
            # session.commit()

            if result.returns_rows:
                columns = result.keys()
                data = [dict(zip(columns, row)) for row in result.fetchall()]
                return data
            else:
                return f"Query {sql_query} executed successfully"

        except Exception as e:
            session.rollback()
            raise e

        finally:
            session.close()
