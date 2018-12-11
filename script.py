from bq_helper import BigQueryHelper
from google.cloud import bigquery


#before executing this code you have to export your key : export GOOGLE_APPLICATION_CREDENTIALS="path to your key.json"


client = bigquery.Client(project='Oceans')


bq_assistant = BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="noaa_icoads")

bq_assistant.list_tables()
bq_assistant.table_schema('icoads_core_2005')

query = """SELECT latitude, longitude, wind_direction_true, wind_speed, present_weather, sea_level_pressure, air_temperature,  wetbulb_temperature, sea_surface_temp,
            total_cloud_amount, cloud_height, wave_direction, wave_period, wave_height, swell_direction, swell_period, swell_height, timestamp
            FROM `bigquery-public-data.noaa_icoads.icoads_core_2005`
                        """

#execute the query.
res = bq_assistant.query_to_pandas_safe(query)

#save the result.
res.to_csv("resultat_total_20052.csv", sep=',')
