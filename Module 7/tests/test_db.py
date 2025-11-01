from sqlalchemy import text


def test_db_session(db_session):
    result = db_session.execute(text("SELECT 1")).scalar()
    assert result == 1
