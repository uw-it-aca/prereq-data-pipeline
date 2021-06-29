from prereq_data_pipeline.dao.edw import get_registrations_since_year
from prereq_data_pipeline.models.registration import Registration
from prereq_data_pipeline.databases.implementation import get_db_implemenation

REGISTRATION_START_YEAR = 2021

def run():
    db = get_db_implemenation()
    session = db.get_session()

    _delete_registrations(session)
    _get_registrations(session)


# get registration data
def _get_registrations(session):
    registrations = get_registrations_since_year(REGISTRATION_START_YEAR)
    chunk_size = 10000
    chunks = [registrations[x:x+chunk_size] for x in
              range(0, len(registrations), chunk_size)]

    # process and save a batch of registrations
    def process_registrations(registrations):
        registration_objects = []
        for index, registration in registrations.iterrows():
            registration_objects.append(
                Registration(
                    system_key=registration['system_key'],
                    regis_yr=registration['regis_yr'],
                    regis_qtr=registration['regis_qtr'],
                    crs_curric_abbr=registration['crs_curric_abbr'],
                    crs_number=registration['crs_number']
                )
            )
        return registration_objects

    for chunk in chunks:
        objs = process_registrations(chunk)
        _save_registrations(session, objs)


# save registration data
def _save_registrations(session, registrations):
    session.add_all(registrations)
    session.commit()


# delete existing registration data
def _delete_registrations(session):
    q = session.query(Registration)
    q.delete()
    session.commit()
