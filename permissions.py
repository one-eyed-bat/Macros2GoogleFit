from jnius import autoclass

activityCompat = autoclass('androidx.core.app.ActivityCompat')
Manifest = autoclass('android.Manifest')
ContextCompat = autoclass('androidx.core.content.ContextCompat')
PackageManager = autorclass('android.content.pm.PackageManager')

activity = autoclass('org.kivy.android.PythonActivity').mActivity

permissions = [
        Manifest.permission.WRITE_EXTERNAL_STORAGE,
        Manifest.permission.READ_EXTERNAL_STORAGE
        ]
for permission in permissions:
    if ContextCompat.checkSelfPermission(activity, permission) != PackageManager.PERMISSION_GRANTED:
        ActivityCompat.requestPermissions(activity, permissions, 1)

