print("\n                                                   Tugas Capstone Modul 1 - RUDI        ")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Deskripsi :")
print("Merepresentasikan Laporan Keuangan sederhana sebuah Perusahaan,")
print("Dimana data Realisasi dan Target telah tersedia, dan Inputan data adalah Realisasi tahun berjalan.")
print("Laporan ini akan disajikan dalam tabel sebagai komulatif / Year to Date")
print("Untuk merepresentasikan koreksi atas laporan audit, maka data ini bisa di edit di fitur update baik realisasi ataupun target")

financial_data = []

#mendefinisikan list kosong untuk menyimpan laporan keuangan bulanan dalam bentuk Dict

# Untuk memudahkan saat create data, target dan realisasi telah tersedia, nantinya data ini bisa di update
# data ini akan menjadi bagian dari bulan jan hingga des

#sebagai acuan target data
monthly_target_revenue = [500, 505, 510, 515, 520, 590, 585, 580, 5150, 5180, 5120, 5200]
monthly_target_direct_material = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_target_direct_labor = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_target_subkon = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_target_overhead = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_target_depre = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]

#sebagai acuan realisasi data th sebelumnya
monthly_realisasi_revenue_2023 = [595, 800, 155, 880, 595, 800, 155, 880, 595, 800, 155, 880,]
monthly_realisasi_direct_material_2023 = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_realisasi_direct_labor_2023 = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_realisasi_subkon_2023 = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_realisasi_overhead_2023 = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]
monthly_realisasi_depre_2023 = [20, 22, 25, 28, 30, 18, 15, 17, 35, 40, 25, 50]

#sebagai acuan realisasi data th saat ini
# monthly_realisasi_revenue_2024 = [95, 100, 105, 110]
# monthly_realisasi_direct_material_2024 = [20, 22, 25, 28, 30]
# monthly_realisasi_direct_labor_2024 = [20, 22, 25, 28, 30]
# monthly_realisasi_subkon_2024 = [20, 22, 25, 28, 30]
# monthly_realisasi_overhead_2024 = [20, 22, 25, 28, 30]
# monthly_realisasi_depre_2024 = [20, 22, 25, 28, 30]


print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Laporan Keuangan Ytd (komulatif)")
        print("2. Membuat Laporan Bulanan Realisasi 2024")
        print("3. Memperbaharui (update) Laporan Bulanan th. 2023 dan th. 2024")
        print("4. Menghapus Laporan Bulanan Realisasi 2024")
        print("5. Keluar")
        choice = input("Silahkan pilih point yang akan dilihat (1-5): ")
        if choice == "1":
            read_ytd_report_menu()  
        elif choice == "2":
            create_monthly_report()  
        elif choice == "3":
            update_monthly_report()  
        elif choice == "4":
            delete_monthly_report()  
        elif choice == "5":
            print("Terimakasih, Silahkan Akses kembali Jika Diperlukan!")
            quit()
        else:
            print("The Option You Entered Is Not Valid.")
            print("Untuk Melanjutkan Pilih Angka Diantara 1 Sampai 5.")

def read_ytd_report_menu():
    while True:
        print("\nRead YTD Report Menu:")
        print("1. Menyajikan Tabel dan Summary Laporan Full Year (Ytd December)")
        print("2. Menyajikan Tabel dan Summary Laporan Ytd Bulan")
        print("3. Kembali ke Menu Utama")
        choice = input("Silahkan pilih point yang akan dilihat (1-3): ")
        if choice == "1":
            display_ytd_table("Desember")  # Menampilkan data hingga bulan terakhir
        elif choice == "2":
            month = get_month_input()
            display_ytd_table(month)  # Menampilkan data hingga bulan tertentu
        elif choice == "3":
            return  # Kembali ke menu utama
        else:
            print("The Option You Entered Is Not Valid.")
            print("Silakan Pilih Angka 1, 2, atau 3.")

# Bagian ini adalah fungsi untuk memasukkan Angka dan harus berupa angka
# jika input bukan angka akan ada looping untuk memastikan inputan harus berupa angka.bisa berupa float
def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Input tidak sesuai, hanya bisa input angka.")

# Bagian ini adalah fungsi untuk memasukkan nama bulan dan harus sesuai dengan yang telah didefinikan
# jika input bukan angka akan ada looping untuk memastikan inputan harus berupa nama Bulan
def get_month_input():
    months_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    while True:
        month = input("Tuliskan Bulan (misal 'Januari', 'Februari', ...): ")
        if month in months_list:
            return month
        else:
            print("Untuk dapat melanjutkan, tuliskan Nama Bulan yang sesuai dan menggunakan huruf kapital di awal.")

# membuat tabel
def display_ytd_table(month):
    if not financial_data:
        print("Data Does Not Exist.")
    #     return
    months_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
  # agar semua bulan dapat diakumulasikan 
    ytd_months = months_list.index(month) + 1

    # sebagai acuan nanti akan dibuat ytd
    ytd_data = {
   
    "Revenue": 0,             
    "Direct material": 0,
    "Direct labor": 0,
    "Subkon": 0,
    "Overhead": 0,
    "Depre": 0,
    "Gross Profit" : 0
}
    month_data_found = False

    months_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    for report in financial_data:
            if months_list.index(report["Month"]) < ytd_months:
                month_data_found = True
                ytd_data["Revenue"] += report["Revenue"]
                ytd_data["Direct material"] += report["Direct material"]
                ytd_data["Direct labor"] += report["Direct labor"]
                ytd_data["Subkon"] += report["Subkon"]
                ytd_data["Overhead"] += report["Overhead"]
                ytd_data["Depre"] += report["Depre"]
                ytd_data["Gross Profit"] += report["Revenue"] - report["Direct material"]-report["Direct labor"]-report["Subkon"]-report["Overhead"]-report["Depre"]
    if not month_data_found:
        print(f"Data Realisasi untuk bulan {month} 2024 belum tersedia. Silahkan Create data realisasi bulanan.")

    # menghitung ytd target
    ytd_target_revenue = sum(monthly_target_revenue[:ytd_months])
    ytd_target_direct_material = sum(monthly_target_direct_material[:ytd_months])
    ytd_target_direct_labor = sum(monthly_target_direct_labor[:ytd_months])
    ytd_target_subkon = sum(monthly_target_subkon[:ytd_months])
    ytd_target_overhead = sum(monthly_target_overhead[:ytd_months])
    ytd_target_depre = sum(monthly_target_depre [:ytd_months])

    ytd_target_gross_profit = ytd_target_revenue - ytd_target_direct_material - ytd_target_direct_labor - ytd_target_subkon - ytd_target_overhead - ytd_target_depre

    # menghitung ytd realiasi 2023
    ytd_realisasi_revenue_2023 = sum(monthly_realisasi_revenue_2023[:ytd_months])
    ytd_realisasi_direct_material_2023= sum(monthly_realisasi_direct_material_2023[:ytd_months])
    ytd_realisasi_direct_labor_2023 = sum(monthly_realisasi_direct_labor_2023[:ytd_months])
    ytd_realisasi_subkon_2023 = sum(monthly_realisasi_subkon_2023[:ytd_months])
    ytd_realisasi_overhead_2023 = sum(monthly_realisasi_overhead_2023[:ytd_months])
    ytd_realisasi_depre_2023= sum(monthly_realisasi_depre_2023[:ytd_months])
   
    ytd_realisasi_gross_profit_2023 = ytd_realisasi_revenue_2023 - ytd_realisasi_direct_material_2023 - ytd_realisasi_direct_labor_2023 - ytd_realisasi_subkon_2023 - ytd_realisasi_overhead_2023 - ytd_realisasi_depre_2023


    # Menghitung achievement rrealisasi 2024 terhadap target 2024
    achievement_revenue = (ytd_data["Revenue"] / ytd_target_revenue) * 100 if ytd_target_revenue != 0 else 0
    achievement_direct_material = (ytd_data["Direct material"] / ytd_target_direct_material) * 100 if ytd_target_direct_material != 0 else 0
    achievement_direct_labor = (ytd_data["Direct labor"] / ytd_target_direct_labor) * 100 if ytd_target_direct_labor != 0 else 0
    achievement_Subkon = (ytd_data["Subkon"] / ytd_target_subkon) * 100 if ytd_target_subkon != 0 else 0
    achievement_Overhead = (ytd_data["Overhead"] / ytd_target_overhead) * 100 if ytd_target_overhead != 0 else 0
    achievement_Depre = (ytd_data["Depre"] / ytd_target_depre) * 100 if ytd_target_depre != 0 else 0
    achievement_gross_profit = (ytd_data["Gross Profit"] / ytd_target_gross_profit) * 100 if ytd_target_gross_profit != 0 else 0

    # Menghitung growth realiasi 2024 terhadap realisasi 2023
    growth_revenue = ((ytd_data["Revenue"] - ytd_realisasi_revenue_2023) / ytd_realisasi_revenue_2023) * 100 if ytd_realisasi_revenue_2023 != 0 else 0
    growth_direct_material = ((ytd_data["Direct material"] - ytd_realisasi_direct_material_2023) / ytd_realisasi_direct_material_2023) * 100 if ytd_realisasi_direct_material_2023 != 0 else 0
    growth_direct_labor = ((ytd_data["Direct labor"] -  ytd_realisasi_direct_labor_2023) /  ytd_realisasi_direct_labor_2023) * 100 if ytd_realisasi_direct_labor_2023 != 0 else 0
    growth_Subkon = ((ytd_data["Subkon"] - ytd_realisasi_subkon_2023 ) / ytd_realisasi_subkon_2023 ) * 100 if  ytd_realisasi_subkon_2023 != 0 else 0
    growth_Overhead = ((ytd_data["Overhead"] - ytd_realisasi_overhead_2023 ) / ytd_realisasi_overhead_2023 ) * 100 if ytd_realisasi_overhead_2023 != 0 else 0
    growth_Depre = ((ytd_data["Depre"] - ytd_realisasi_depre_2023) / ytd_realisasi_depre_2023) * 100 if ytd_realisasi_depre_2023 != 0 else 0

    growth_gross_profit = ((ytd_data["Gross Profit"] - ytd_realisasi_gross_profit_2023) / ytd_realisasi_gross_profit_2023) * 100 if ytd_realisasi_gross_profit_2023 != 0 else 0



    # menghitung GPM untuk realiasi 2024 target 2024 dan realisasi 2023
    gpm_revenue_2024 = (ytd_data["Gross Profit"] / ytd_data["Revenue"]) * 100 if ytd_data["Revenue"] != 0 else 0
    gpm_revenue_2023 = (ytd_realisasi_gross_profit_2023 / ytd_realisasi_revenue_2023) * 100 if ytd_realisasi_revenue_2023 != 0 else 0
    gpm_revenue_target = (ytd_target_gross_profit / ytd_target_revenue) * 100 if ytd_target_revenue != 0 else 0

    # nampilin tabel
    print(f"\nYTD Report {month} 2024\n")
    print(f"{'Item PL ':<20} | {'YTD Realisasi 2024':<15} | {'YTD Target 2024':<15} | {'YTD Realisasi 2023':<15} | {'Achievement (%)':<15} | {'Growth (%)':<15}")
    print("-" * 130)
    print(f"{'Revenue':<20} | {ytd_data['Revenue']:>18.2f} | {ytd_target_revenue:>15.2f} | {ytd_realisasi_revenue_2023:>18.2f} | {achievement_revenue:<15.2f} | {growth_revenue:<15.2f}")
    print(f"{'Direct material':<20} | {ytd_data['Direct material']:>18.2f} | {ytd_target_direct_material:>15.2f} | {ytd_realisasi_direct_material_2023:>18.2f} | {achievement_direct_material:<15.2f} | {growth_direct_material:<15.2f}")
    print(f"{'Direct labor':<20} | {ytd_data['Direct labor']:>18.2f} | {ytd_target_direct_labor:>15.2f} | { ytd_realisasi_direct_labor_2023:>18.2f} | {achievement_direct_labor:<15.2f} | {growth_direct_labor:<15.2f}")
    print(f"{'Subkon':<20} | {ytd_data['Subkon']:>18.2f} | {ytd_target_subkon:>15.2f} | { ytd_realisasi_subkon_2023:>18.2f} | {achievement_Subkon:<15.2f} | {growth_Subkon:<15.2f}")
    print(f"{'Overhead':<20} | {ytd_data['Overhead']:>18.2f} | {ytd_target_overhead:>15.2f} | {ytd_realisasi_overhead_2023:>18.2f} | {achievement_Overhead:<15.2f} | {growth_Overhead:<15.2f}")
    print(f"{'Depre':<20} | {ytd_data['Depre']:>18.2f} | {ytd_target_depre:>15.2f} | { ytd_realisasi_depre_2023:>18.2f} | {achievement_Depre:<15.2f} | {growth_Depre:<15.2f}")
    print(f"{'Gross Profit':<20} | {ytd_data['Gross Profit']:>18.2f} | {ytd_target_gross_profit:>15.2f} | {ytd_realisasi_gross_profit_2023:>18.2f} | {achievement_gross_profit:<15.2f} | {growth_gross_profit:<15.2f}")
    print(f"{'GPM (%)':<20} | {gpm_revenue_2024:>18.2f} | {gpm_revenue_target:>15.2f} | {gpm_revenue_2023:>18.2f} | {'':<15} | {'':<15}")

    if not month_data_found:
        print(f"Data Realisasi bulan {month} 2024 tidak tersedia, namun tabel tetap ditampilkan. Silahkan Create data realisasi bulanan.")

    # untuk summary report
    revenue_achievement_status = "Mencapai" if achievement_revenue >= 100 else "Tidak Mencapai"
    growth_revenue_status = "Tumbuh" if growth_revenue > 0 else "Tidak Tumbuh"
    
    GrossProfit_achievement_status = "Mencapai" if achievement_gross_profit >= 100 else "Tidak Mencapai"
    growth_GrossProfit_status = "Tumbuh" if growth_gross_profit > 0 else "Tidak Tumbuh"
    print(f"\nSummary Laporan Keuangan Ytd {month} 2024 sebagai berikut :")
    print(f"Revenue Realisasi YTD {month} 2024 '{revenue_achievement_status}' terhadap Target YTD {month} 2024 dan '{growth_revenue_status}' terhadap Realisasi YTD {month} 2023.")
    print(f"Gross Profit Realisasi YTD {month} 2024 '{GrossProfit_achievement_status}' terhadap Target YTD {month} 2024 dan '{growth_GrossProfit_status}' terhadap Realisasi YTD {month} 2023.")
# 
# Fitur Create
def create_monthly_report() :
   while True:
        print("\nSilahkan Pilih Menu yang Diperlukan:")
        print("1. Membuat Laporan Realisasi 2024")
        print("2. Kembali ke Menu Utama")
        choice = input("Silahkan masukkan pilihan (1-2): ")
        
        if choice == "1":
            month = get_month_input()  # Meminta bulan yang ingin dipilih
            
            # Cek apakah data sudah ada untuk bulan tersebut
            if any(report["Month"] == month for report in financial_data):
                print(f"Data for {month} already exists.")
            else:
                # Jika data belum ada, input untuk Revenue dan COGS
                revenue = get_numeric_input(f"Tuliskan Revenue Realisasi {month} 2024: ")
                direct_material = get_numeric_input(f"Tuliskan Direct Matrerial Realisasi {month} 2024: ")
                direct_labor = get_numeric_input(f"Tuliskan Direct Labor Realisasi {month} 2024: ")
                subkon = get_numeric_input(f"Tuliskan Subkon Realisasi {month} 2024: ")
                overhead = get_numeric_input(f"Tuliskan Overhead Realisasi {month} 2024: ")
                depre = get_numeric_input(f"Tuliskan Depre Realisasi {month} 2024: ")
                
                print(f"Revenue: {revenue}")
                print(f"Direct material : {direct_material}")
                print(f"Direct labor: {direct_labor}")
                print(f"Subkon: {subkon}")
                print(f"Overhead: {overhead}")
                print(f"Depre: {depre}")
            

                
                # konfirmasi nyimpen data
                while True:
                    save_choice = input("Do you want to save this data? (Y/N): ").strip().upper()
                    if save_choice == "Y":
                        financial_data.append({
                            "Month": month,
                            "Revenue": revenue,
                            "Direct material" : direct_material,
                            "Direct labor": direct_labor,
                            "Subkon": subkon,
                            "Overhead": overhead,
                            "Depre": depre
                        })
                        print(f"Laporan Realisasi Bulan {month} 2024 telah dibuat dan Data successfully saved.")
                        break
                    elif save_choice == "N":
                        print(f"Data Relisasi {month} 2024 tidak disimpan. kembali ke Menu Pembuatan Laporan.")
                        break
                    else:
                        print("Tuliskan Y atau N.")
        
        elif choice == "2":
            return  
        else:
            print("Inputan salah, Mohon menuliskan angka 1 atau 2.")

#fitur update
def update_monthly_report():
    
    while True:
    
        print("\nPilih Data yang Perlu Diperbaharui (Update):")
        print("1. Update Realisasi 2024")
        print("2. Update Target 2024")
        print("3. Update Realisasi 2023")
        print("4. Update Realisasi 2024, Target 2024, Realisasi 2023")
        print("5. Menu Utama")
        choice = input("masukkan pilihan (1, 2, 3, 4, atau 5): ")
        
        if choice == "1":
                month = get_month_input() 
                month_exists = any(report["Month"] == month for report in financial_data)  # Mengecek apakah ada laporan dengan bulan yang sesuai
                
                print(f"\nData untuk {month}:")
                for report in financial_data:
                    if report["Month"] == month:
                        print(f"Revenue: {report['Revenue']}, Direct material: {report['Direct material']}, Direct labor: {report['Direct labor']}, Subkon: {report['Subkon']}, Overhead: {report['Overhead']}, Depre: {report['Depre']}")

                      
                if month_exists:
               
                    while True:
                        update_choice = input("Apakah akan melanjutkan proses ini? (Y/N): ").strip().upper()
                        if update_choice == "Y":
                            new_revenue = get_numeric_input(f"Masukan Revenue Realisasi bulan {month} 2024: ")
                            new_direct_material = get_numeric_input(f"Masukan Direct Material Realisasi bulan {month} 2024: ")
                            new_direct_labor = get_numeric_input(f"Masukan Direct Labor Realisasi bulan {month} 2024: ")
                            new_subkon = get_numeric_input(f"Masukan Subkon Realisasi bulan {month} 2024: ")
                            new_overhead = get_numeric_input(f"Masukan Overhead Realisasi bulan {month} 2024: ")
                            new_depre = get_numeric_input(f"Masukan Depre Realisasi bulan {month} 2024: ")
                            
                            update_choice = input("Apakah kami akan mengupdate data ini? (Y/N): ").strip().upper()
                            if update_choice == "Y":
                                report["Revenue"] = new_revenue
                                report["Direct material"] = new_direct_material
                                report["Direct labor"] = new_direct_labor 
                                report["Subkon"] = new_subkon
                                report["Overhead"] = new_overhead
                                report["Depre"] = new_depre

                                print(f"Realisasi bulan {month} 2024 updated successfully.") 
                                break
                            elif update_choice == "N":
                                print(f"Data {month} tidak diupdate. kembali ke menu update.")
                            break
                                                                             
                        elif update_choice == "N":
                            print(f"Data {month}tidak diupdate. kembali ke menu update.")
                            break
                        else:
                            print("Invalid choice, returning to menu.")
                    
                else:
                
                    print(f"Data for {month} does not exist.") 


        elif choice == "2":
            month = get_month_input() 
            months_list = ["Desember", "November", "Oktober", "September", "Agustus",
                   "Juli", "Juni", "Mei", "April", "Maret", "Februari","Januari"]
            target_month = months_list.index(month)
            new_target_revenue = get_numeric_input(f"Masukan Revenue target bulan {month} 2024: ")
            new_target_direct_material = get_numeric_input(f"Masukan Direct Material target bulan {month} 2024: ")
            new_target_direct_labor = get_numeric_input(f"Masukan Direct Labor target bulan {month} 2024: ")
            new_target_subkon = get_numeric_input(f"Masukan Subkon target bulan {month} 2024: ")
            new_target_overhead = get_numeric_input(f"Masukan Overhead target bulan {month} 2024: ")
            new_target_depre = get_numeric_input(f"Masukan Depre target bulan {month} 2024: ")

            monthly_target_revenue[target_month] = new_target_revenue
            monthly_target_direct_material[target_month] = new_target_direct_material
            monthly_target_direct_labor [target_month] = new_target_direct_labor
            monthly_target_subkon[target_month] = new_target_subkon
            monthly_target_overhead[target_month] = new_target_overhead
            monthly_target_depre[target_month] = new_target_depre

            print(f"Target bulan {month} 2024 updated successfully.")
        

        elif choice == "3":
            month = get_month_input() 
            months_list = ["Desember", "November", "Oktober", "September", "Agustus",
                   "Juli", "Juni", "Mei", "April", "Maret", "Februari","Januari"]
            target_month = months_list.index(month)
            new_realisasi_revenue_2023 = get_numeric_input(f"Masukan Revenue Realisasi bulan {month} 2023: ")
            new_realisasi_direct_material_2023 = get_numeric_input(f"Masukan Direct Material Realisasi bulan {month} 2023: ")
            new_realisasi_direct_labor_2023 = get_numeric_input(f"Masukan Direct Labor Realisasi bulan {month} 2023: ")
            new_realisasi_subkon_2023 = get_numeric_input(f"Masukan Subkon Realisasi bulan {month} 2023: ")
            new_realisasi_overhead_2023 = get_numeric_input(f"Masukan Overhead Realisasi bulan {month} 2023: ")
            new_realisasi_depre_2023 = get_numeric_input(f"Masukan Depre Realisasi bulan {month} 2023: ")
            
            monthly_realisasi_revenue_2023[target_month] = new_realisasi_revenue_2023
            monthly_realisasi_direct_material_2023[target_month] = new_realisasi_direct_material_2023
            monthly_realisasi_direct_labor_2023[target_month] = new_realisasi_direct_labor_2023
            monthly_realisasi_subkon_2023[target_month] = new_realisasi_subkon_2023
            monthly_realisasi_overhead_2023[target_month] = new_realisasi_overhead_2023
            monthly_realisasi_depre_2023[target_month] = new_realisasi_depre_2023
           

            print(f"Realisasi {month} 2023 updated successfully.")



        elif choice == "4":
            month = get_month_input() 
            for report in financial_data:
                if report["Month"] == month:
                    new_revenue = get_numeric_input(f"Masukan Revenue Realisasi bulan {month} 2024: ")
                    new_direct_material = get_numeric_input(f"Masukan Direct Material Realisasi bulan {month} 2024: ")
                    new_direct_labor = get_numeric_input(f"Masukan Direct Labor Realisasi bulan {month} 2024: ")
                    new_subkon = get_numeric_input(f"Masukan Subkon Realisasi bulan {month} 2024: ")
                    new_overhead = get_numeric_input(f"Masukan Overhead Realisasi bulan {month} 2024: ")
                    new_depre = get_numeric_input(f"Masukan Depre Realisasi bulan {month} 2024: ")
                    report["Revenue"] = new_revenue
                    report["Direct material"] = new_direct_material
                    report["Direct labor"] = new_direct_labor 
                    report["Subkon"] = new_subkon
                    report["Overhead"] = new_overhead
                    report["Depre"] = new_depre
                    print(f"Realisasi bulan {month} updated successfully.")
            
            months_list = ["Desember", "November", "Oktober", "September", "Agustus",
                   "Juli", "Juni", "Mei", "April", "Maret", "Februari","Januari"]
            target_month = months_list.index(month)
            new_target_revenue = get_numeric_input(f"Masukan Revenue target bulan {month} 2024: ")
            new_target_direct_material = get_numeric_input(f"Masukan Direct Material target bulan {month} 2024: ")
            new_target_direct_labor = get_numeric_input(f"Masukan Direct Labor target bulan {month} 2024: ")
            new_target_subkon = get_numeric_input(f"Masukan Subkon target bulan {month} 2024: ")
            new_target_overhead = get_numeric_input(f"Masukan Overhead target bulan {month} 2024: ")
            new_target_depre = get_numeric_input(f"Masukan Depre target bulan {month} 2024: ")

            monthly_target_revenue[target_month] = new_target_revenue
            monthly_target_direct_material[target_month] = new_target_direct_material
            monthly_target_direct_labor [target_month] = new_target_direct_labor
            monthly_target_subkon[target_month] = new_target_subkon
            monthly_target_overhead[target_month] = new_target_overhead
            monthly_target_depre[target_month] = new_target_depre
            print(f"Target bulan {month} 2024 updated successfully.")
            
            new_realisasi_revenue_2023 = get_numeric_input(f"Masukan Revenue Realisasi bulan {month} 2023: ")
            new_realisasi_direct_material_2023 = get_numeric_input(f"Masukan Direct Material Realisasi bulan {month} 2023: ")
            new_realisasi_direct_labor_2023 = get_numeric_input(f"Masukan Direct Labor Realisasi bulan {month} 2023: ")
            new_realisasi_subkon_2023 = get_numeric_input(f"Masukan Subkon Realisasi bulan {month} 2023: ")
            new_realisasi_overhead_2023 = get_numeric_input(f"Masukan Overhead Realisasi bulan {month} 2023: ")
            new_realisasi_depre_2023 = get_numeric_input(f"Masukan Depre Realisasi bulan {month} 2023: ")
            
            monthly_realisasi_revenue_2023[target_month] = new_realisasi_revenue_2023
            monthly_realisasi_direct_material_2023[target_month] = new_realisasi_direct_material_2023
            monthly_realisasi_direct_labor_2023[target_month] = new_realisasi_direct_labor_2023
            monthly_realisasi_subkon_2023[target_month] = new_realisasi_subkon_2023
            monthly_realisasi_overhead_2023[target_month] = new_realisasi_overhead_2023
            monthly_realisasi_depre_2023[target_month] = new_realisasi_depre_2023
            print(f"Realisasi bulan {month} 2023 updated successfully.")
        
        elif choice == "5":
            return  # Kembali ke menu utama
        else:
            print("Pilihan salah, pilih 1, 2, 3, 4 atau 5.")


# Fitur delete
def  delete_monthly_report():

    
    while True:
        print("\nMenghapus laporan bulan tertentu:")
        print("1. Menghapus laporan bulan tertentu ")
        print("2. kembali ke menu utama")
        choice = input("Pilih (1-2): ")
        
        if choice == "1":
            month = get_month_input()  
            global financial_data 
    
          
            month_exists = any(report["Month"] == month for report in financial_data)  

            print(f"\nData untuk {month}:")
            for report in financial_data:
                if report["Month"] == month:
                    print(f"Revenue: {report['Revenue']}, Direct Material: {report['Direct Material']}, Direct labor: {report['Direct labor']}, Subkon: {report['Subkon']}, Overhead: {report['Overhead']}, Depre: {report['Depre']}")
            if month_exists:
            
                while True:
                    delete_choice = input("Apakah kamu ingin menhapus data ini ? (Y/N): ").strip().upper()
                    if delete_choice == "Y":
                        financial_data = [report for report in financial_data if report["Month"] != month]
                        print(f"Laporan bulan {month} deleted successfully.")  
                        break
                    elif delete_choice == "N":
                        print(f"Data for {month} not deleted. kwmalike menu delete.")
                        break
                    else:
                        print("pilihan salah, kembali.")
                
            else:
            
                print(f"Data for {month} does not exist.")  
        
        elif choice == "2":
            return  # Kembali ke menu utama
        else:
            print("Pilihan salah, silahkan pilih 1 atau 2.")


# Run the program
main_menu()