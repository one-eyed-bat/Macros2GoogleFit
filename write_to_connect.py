from jnius import autoclass
from datetime import datetime

HealthConnectClient = autoclass('androidx.health.connect.client.HealthConnectClient')
DataType = autoclass('androidx.health.connect.client.records.DataType')
HealthRecord = autoclass('androidx.health.connect.client.records.HealthRecord')

context = autoclass('org.kivy.android.PythonActivity').mActivity
health_connect_client = HealthConnectClient.getOrCreate(context)

macros_record = HealthRecord.Builder(DataType.NUTRITION)
now = datetime.now().isoformat()
macros_record.setStartTime(now)
macros_record.setEndTime(now)

carbs = 50
protein = 30 
fat = 10

macros_record.setValue('Carbs', carbs)
macros_record.setValue('protein', protein)
macros_record.setValue('fat', fat)

health_connect_client.insertRecords([macros_record.build()])
