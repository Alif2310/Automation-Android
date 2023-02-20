#utama 
import logging
from logging.handlers import BaseRotatingHandler
from appium import webdriver
import re

#Menunggu sampai dengan ......
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

#Untuk Action Touch doble atau single atau tahan atau dll
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.common.action_chains import ActionChains

#from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException

#waktu secara static / 
import time


desired_caps = {}
desired_caps ["platformName"] = "Android"
desired_caps ["udid"] = "de372c98"
desired_caps ["deviceName"] = "device"
desired_caps ["appPackage"] = "org.owline.kasirpintarpro"
desired_caps ["appActivity"] = "org.owline.kasirpintarpro.SplashScreen"
#
# # org.owline.kasirpintarpro
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.implicitly_wait(10)
# klik button Login
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/tv_login").click()

# Login Ketika required/email dan PW tidak di isi\
driver.implicitly_wait(5)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()


# # Login salah password
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").send_keys("alifkaspin1@gmail.com")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").send_keys("alif23")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_OK").click()

# Login salah email
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").send_keys("alifkaspin12222@gmail.com")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").send_keys("alif23")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_OK").click()

# # Login Email invalid/Format email tidak sesuai standarisasi
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").send_keys("alifkaspin1.@gmail.com")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()


# login normal
time.sleep(1)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_email").send_keys("alifkaspin1@gmail.com")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").click()
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/edt_password").send_keys("alif2310")
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_login").click()

nunggu_lama = WebDriverWait(driver, 100) #second
nunggu_cepat = WebDriverWait(driver, 1)


wait50 = driver.implicitly_wait(100)

#pop up get devices
try:
    driver.implicitly_wait(100)
    driver.find_element(By.ID,"org.owline.kasirpintarpro:id/ya").click()
except :
    pass

try:
    nunggu_lama.until(EC.presence_of_element_located((By.ID, "org.owline.kasirpintarpro:id/btn_ok")))
    driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_ok").click()
except :
    pass

try:
    driver.implicitly_wait(10)
    driver.find_element(By. ID,"com.android.permissioncontroller:id/permission_allow_button").click()
except:
    pass

#Pilih Bulan
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]").click()

try:
    driver.implicitly_wait(1)
    driver.find_element(By. ID,"com.android.permissioncontroller:id/permission_allow_button").click()
except:
    pass

#3baris untuk membuka sidebar
driver.implicitly_wait(50)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/bars").click()
# buka profil
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/nama_user").click()
# klik button logout sampai berhasil
driver.implicitly_wait(10)
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/tv_logout").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/rb_logout").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/btn_next").click()

# Login lagi
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/tv_login").click()

# Pilih akun google yang belum terdaftar
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/imgbtn_google").click()
driver.find_element(By.XPATH,"//android.widget.TextView[@text='Alif Indramawan']").click()
driver.implicitly_wait(10)
driver.find_element(By. ID,"org.owline.kasirpintarpro:id/btn_OK").click()

# Pilih akun google yang sudah terdaftar
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/imgbtn_google").click()
driver.find_element(By.XPATH,"//android.widget.TextView[@text='alif kaspin1']").click()

#pop up get devices
try:
    driver.implicitly_wait(5)
    driver.find_element(By.ID,"org.owline.kasirpintarpro:id/ya").click()
except :
    pass

try:
    nunggu_lama.until(EC.presence_of_element_located((By.ID, "org.owline.kasirpintarpro:id/btn_ok")))
    driver.find_element(By.ID,"org.owline.kasirpintarpro:id/btn_ok").click()
except :
    pass

try:
    driver.implicitly_wait(1)
    driver.find_element(By. ID,"com.android.permissioncontroller:id/permission_allow_button").click()
except:
    pass

#Pilih Bulan
time.sleep(5)
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]").click()

try:
    driver.implicitly_wait(1)
    driver.find_element(By. ID,"com.android.permissioncontroller:id/permission_allow_button").click()
except:
    pass


# Klik Baarang di menu manajemen 
driver.implicitly_wait(100)
driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()

# # pop up update ke next fitur
try:
    driver.implicitly_wait(1)
    driver.find_element(By. ID,"org.owline.kasirpintarpro:id/nanti").click()
except:
    pass

# # klik tambah Barang 
driver.implicitly_wait(50)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/fab").click()

# mengisi data barang 
driver.implicitly_wait(50)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editNamaBarang").send_keys("barang baru 3")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editJumlah").send_keys("100")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editKodeBarang").send_keys("baru3")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editHargaBeli").send_keys("1000")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/editHargaJual").send_keys("5000")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btnTambahDataBarang").click()

# button back ke halaman manajemen 
driver.implicitly_wait(50)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linear_back").click()

#3baris untuk membuka sidebar
driver.implicitly_wait(50)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/bars").click()

#Menu transaksi Penjualan di sidebar
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/lin_transaksi").click()   


# klik pencarian
driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/act_search_product").send_keys("barang baru 3")

# pilih barang "baru"
actions = TouchAction(driver)
actions.long_press(driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView")).release().perform()

#klik nominal 
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tambah_barang").click()

#klik checkbox ubah harga sementara
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/checkBox2").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_harga").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_harga").clear()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_harga").send_keys("3000")

# ubah diskon perbarang
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/checkBox3").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_diskon").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_diskon").clear()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ubah_diskon").send_keys("50")

# Tutup pop up barang
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/lanjut").click()

# Lanjut ke halaman keranjang
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tv_count_cart").click()

#Menambahkan Biaya Ongkir
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linear_add_biaya").click()
driver.implicitly_wait(100)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_modul_ongkir").click()
driver.implicitly_wait(100)
driver.find_element(By. XPATH, ("//android.widget.TextView[@text='Pilih Provinsi']")).click()
driver.implicitly_wait(100)
driver.find_element(By. XPATH, ("//android.widget.TextView[@text='Bali']")).click()
driver.implicitly_wait(100)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/spinner_pengiriman").click()
driver.implicitly_wait(100)
driver.find_element(By. XPATH, ("//android.widget.TextView[@text='JNE']")).click()
driver.implicitly_wait(100)
driver.find_element(By. XPATH, ("//android.widget.TextView[@text='Rp 23,000']")).is_displayed()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btn_ok").click()

# Lanjut ke halaman Pembayaran dengan klik Bayar
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linear_bayar").click()

# Input Diskon di halaman Pembayaran 
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearDiskon").click()
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/edit_diskon").click()
driver.back()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/edit_diskon").clear()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/edit_diskon").send_keys("50")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tombol_diskon").click()

#Input Pajak di halaman Pembayaran
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearPajak").click()
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/rb_tax_manual").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/et_tax").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/et_tax").send_keys("100")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tombol_pajak").click()

#input pembayaran dengan papan uang -> dengan uang pas   
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/tampil_papan_uang").click()
driver.find_element(By. XPATH, ("//android.widget.TextView[@text='Uang Pas']")).click() 

#input Catatan Pertransaksi
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearKeterangan").click()
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/isi").click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/isi").send_keys("Catatan Transaksi Tes")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/ya").click()

#klik centang untuk menyelesaikan pembayaran
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearProses").click()

#klik lihat struk
driver.implicitly_wait(10)
driver.find_element(By. XPATH,("//android.widget.TextView[@text='More']")).click()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearDetailStruk").click()

#Menunggu menampilkan struk
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/nama_toko").is_displayed()

# back dari struk
driver.back()
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/btnSelesai").click()

# ke halaman barang untuk menghapus barang
driver.implicitly_wait(5)
driver.find_element(By.ID,"org.owline.kasirpintarpro:id/bars").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/lin_manajemen").click()
driver.find_element(By. XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView").click()
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/cari_barang").send_keys("barang baru 3")
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linierBarang").click()
driver.implicitly_wait(10)
driver.find_element(By. ID, "org.owline.kasirpintarpro:id/linearHapus").click()
driver.implicitly_wait(10)
driver.find_element(By.ID, "org.owline.kasirpintarpro:id/ya").click()
