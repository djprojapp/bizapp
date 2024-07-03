# Generated by Django 5.0 on 2024-06-05 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("insbiz", "0003_alter_bankdetail_doctor_alter_status_doctor"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="hospital",
            field=models.CharField(
                choices=[
                    (
                        "Punjab Institute of Cardiology, Lahore",
                        "Punjab Institute of Cardiology, Lahore",
                    ),
                    (
                        "Faisalabad Institute of Cardiology, Faisalabad",
                        "Faisalabad Institute of Cardiology, Faisalabad",
                    ),
                    ("Mayo Hospital, Lahore", "Mayo Hospital, Lahore"),
                    ("Nishtar Hospital, Multan", "Nishtar Hospital, Multan"),
                    (
                        "Bahawal Victoria Hospital, Bahawalpur",
                        "Bahawal Victoria Hospital, Bahawalpur",
                    ),
                    ("Jinnah Hospital, Lahore", "Jinnah Hospital, Lahore"),
                    (
                        "Lahore General Hospital, Lahore",
                        "Lahore General Hospital, Lahore",
                    ),
                    ("Allied Hospital, Faisalabad", "Allied Hospital, Faisalabad"),
                    ("DHQ Hospital, Gujranwala", "DHQ Hospital, Gujranwala"),
                    (
                        "Punjab Dental Hospital, Lahore",
                        "Punjab Dental Hospital, Lahore",
                    ),
                    ("Children Hospital, Lahore", "Children Hospital, Lahore"),
                    ("Services Hospital, Lahore", "Services Hospital, Lahore"),
                    ("Children Hospital, Multan", "Children Hospital, Multan"),
                    ("DHQ Rawalpindi", "DHQ Rawalpindi"),
                    (
                        "Sheikh Zayed Medical Complex, Rahim Yar Khan",
                        "Sheikh Zayed Medical Complex, Rahim Yar Khan",
                    ),
                    (
                        "Benazir Bhutto Hospital, Rawalpindi",
                        "Benazir Bhutto Hospital, Rawalpindi",
                    ),
                    (
                        "Sir Ganga Ram Hospital, Lahore",
                        "Sir Ganga Ram Hospital, Lahore",
                    ),
                    ("DHQ Hospital, Faisalabad", "DHQ Hospital, Faisalabad"),
                    ("AIMH, Sialkot", "AIMH, Sialkot"),
                    (
                        "DHQ Teaching Hospital, Sargodha",
                        "DHQ Teaching Hospital, Sargodha",
                    ),
                    (
                        "Choudhary Prevez Ilahi Institute of Cardiology, Multan",
                        "Choudhary Prevez Ilahi Institute of Cardiology, Multan",
                    ),
                    ("ABS Teaching Hospital, Gujrat", "ABS Teaching Hospital, Gujrat"),
                    (
                        "Holy Family Hospital, Rawalpindi",
                        "Holy Family Hospital, Rawalpindi",
                    ),
                    (
                        "Institute of Child Health, Faisalabad",
                        "Institute of Child Health, Faisalabad",
                    ),
                    (
                        "Wazirabad Institute of Cardiology, Warzirabad",
                        "Wazirabad Institute of Cardiology, Warzirabad",
                    ),
                    ("DHQ Hospital, DG Khan", "DHQ Hospital, DG Khan"),
                    ("Lady Willingdon Hospital", "Lady Willingdon Hospital"),
                    (
                        "Nishtar Institute of Dentistry, Multan",
                        "Nishtar Institute of Dentistry, Multan",
                    ),
                    (
                        "Sahiwal Teaching Hospital, Sahiwal",
                        "Sahiwal Teaching Hospital, Sahiwal",
                    ),
                    (
                        "Govt. Teaching Hospital, Shahdra, Lahore",
                        "Govt. Teaching Hospital, Shahdra, Lahore",
                    ),
                    (
                        "Punjab Institute of Neurosciences, Lahore",
                        "Punjab Institute of Neurosciences, Lahore",
                    ),
                    (
                        "Rawalpindi Institute of Cardiology, Rawalpindi",
                        "Rawalpindi Institute of Cardiology, Rawalpindi",
                    ),
                    (
                        "RMU Allied Hospital, Rawalpindi",
                        "RMU Allied Hospital, Rawalpindi",
                    ),
                    (
                        "Kot Khawaja Saeed Hospital, Lahore",
                        "Kot Khawaja Saeed Hospital, Lahore",
                    ),
                    ("Civil Hospital Bahawalpur", "Civil Hospital Bahawalpur"),
                    ("Lady Aitchison Hospital", "Lady Aitchison Hospital"),
                    (
                        "Allied Hospital (Dentistry), Faisalabad",
                        "Allied Hospital (Dentistry), Faisalabad",
                    ),
                    (
                        "Govt. Teaching Hospital GM Abad, Faisalabad",
                        "Govt. Teaching Hospital GM Abad, Faisalabad",
                    ),
                    ("DHQ, Mianwali", "DHQ, Mianwali"),
                    ("DHQ Hospital, Jhang", "DHQ Hospital, Jhang"),
                    (
                        "Punjab Institute of Mental Health, Lahore",
                        "Punjab Institute of Mental Health, Lahore",
                    ),
                    ("DHQ Hospital, Mandi Bahauddin", "DHQ Hospital, Mandi Bahauddin"),
                    (
                        "Combined Military Hospital, Lahore",
                        "Combined Military Hospital, Lahore",
                    ),
                    (
                        "Isfandyar Bukhari/ DHQ Hospital, Attock",
                        "Isfandyar Bukhari/ DHQ Hospital, Attock",
                    ),
                    (
                        "Institute Of Public Health (IPH) Lahore",
                        "Institute Of Public Health (IPH) Lahore",
                    ),
                ],
                max_length=225,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="doctor",
            name="speciality",
            field=models.CharField(
                choices=[
                    ("Cardiology", "Cardiology"),
                    ("Medicine", "Medicine"),
                    ("Plastic Surgery", "Plastic Surgery"),
                    ("Neurology", "Neurology"),
                    ("Pediatrics", "Pediatrics"),
                    ("Ophthalmology", "Ophthalmology"),
                    ("Orthopedic Surgery", "Orthopedic Surgery"),
                    ("General Surgery", "General Surgery"),
                    ("Obstetrics & Gynecology", "Obstetrics & Gynecology"),
                    ("Neuro Surgery", "Neuro Surgery"),
                    ("Otorhinolaryngology ENT", "Otorhinolaryngology ENT"),
                    ("Anaesthesia", "Anaesthesia"),
                    ("Orthodontics", "Orthodontics"),
                    ("Operative Dentistry", "Operative Dentistry"),
                    ("Hematology", "Hematology"),
                    ("Radiology", "Radiology"),
                    ("Nephrology", "Nephrology"),
                    ("Diagnostic Radiology", "Diagnostic Radiology"),
                    ("Oral & Maxillofacial Surgery", "Oral & Maxillofacial Surgery"),
                    ("General Medicine", "General Medicine"),
                    ("Emergency Medicine", "Emergency Medicine"),
                    ("Chemical Pathology", "Chemical Pathology"),
                    ("Urology", "Urology"),
                    ("Thoracic Surgery", "Thoracic Surgery"),
                    ("Pulmonology", "Pulmonology"),
                    ("Psychiatry", "Psychiatry"),
                    ("Cardiac Surgery", "Cardiac Surgery"),
                    ("Dermatology", "Dermatology"),
                    ("Community Medicine", "Community Medicine"),
                    ("Cardio Thoracic Anesthesia", "Cardio Thoracic Anesthesia"),
                    ("Pediatric Surgery", "Pediatric Surgery"),
                    ("Histopathology", "Histopathology"),
                    ("Medical Oncology", "Medical Oncology"),
                    ("Gastroenterology", "Gastroenterology"),
                    ("Orthopaedic", "Orthopaedic"),
                    ("Physiology", "Physiology"),
                    ("Prosthodontics", "Prosthodontics"),
                    ("Radiotherapy", "Radiotherapy"),
                    ("Chest Surgery", "Chest Surgery"),
                    ("Forensic Medicine", "Forensic Medicine"),
                    ("Biochemistry", "Biochemistry"),
                    ("Accident & Emergency", "Accident & Emergency"),
                    ("Anatomy", "Anatomy"),
                    ("Pharmacology", "Pharmacology"),
                    ("Family Dentistry", "Family Dentistry"),
                    ("Endocrinology", "Endocrinology"),
                    ("Clinical Histopathology", "Clinical Histopathology"),
                    (
                        "Paediatrics / Paediatrics Medicine",
                        "Paediatrics / Paediatrics Medicine",
                    ),
                ],
                max_length=225,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="bankdetail",
            name="bank",
            field=models.CharField(
                choices=[
                    ("UBL", "United Bank Ltd"),
                    ("HBL", "Habib Bank Ltd"),
                    ("BOP", "Bank of Punjab"),
                    ("MCB", "Muslim Commercial Bank"),
                    ("ABL", "Allied Bank Ltd"),
                    ("BAH", "Bank Al-Habib"),
                    ("BAF", "Bank Alfalah"),
                    ("MZN", "Meezan Bank"),
                    ("NBP", "National Bank of Pakistan"),
                    ("JSB", "JS Bank"),
                    ("BIL", "Bank Islami Ltd"),
                    ("ASB", "Askri Bank"),
                    ("HMB", "Habib Metro Bank"),
                    ("FBL", "Faysal Bank Ltd"),
                    ("SCB", "Standard Chartered Bank"),
                    ("FWBL", "First Women Bank Ltd"),
                    ("CBL", "Citi Bank Ltd"),
                    ("DIB", "Dubai Islamic Bank"),
                    ("BOK", "Bank of Khyber"),
                    ("SBL", "Sind Bank Ltd"),
                    ("ABB", "Al-Barkha Bank"),
                    ("MIB", "MCB Islamic"),
                ],
                max_length=225,
            ),
        ),
    ]
