    dev_appserver.py --datastore_path='./tmp/datastore.db' ./

Use the following command to deploy:
    gcloud auth login (first time)
    gcloud app deploy --project brianlininfo

Make Sure the admin login setting
    - url: /admin_page.*
      script: scripts.main.application 
      login: admin
      secure: always
      auth_fail_action: redirect
    - url: /form.*
      script: scripts.form.application 
      login: admin
      secure: always
