#PROGRAM UTAMA
if __name__ == '__main__':
    def getAxis(data):
        #Mendapatkan index sumbu yang akan diproses
        print("Daftar Kolom di Dataset")
        for i in range(len(df.columns)):
            print(i+1,".",df.columns[i])
        while(True):
            sumbu_x = int(input("Pilih nomor kolom yang ingin menjadi sumbu-x: "))
            if(sumbu_x>=1 and sumbu_x<=len(df.columns)):
                break
            else:
                print("Pilihan tidak valid!")
        while(True):
            sumbu_y = int(input("Pilih nomor kolom yang ingin menjadi sumbu-y: "))
            if(sumbu_y>=1 and sumbu_y<=len(df.columns)and sumbu_x!=sumbu_y):
                break
            else:
                print("Pilihan tidak valid!")
        return (sumbu_x-1,sumbu_y-1)

    import pandas as pd
    import matplotlib.pyplot as plt
    import myConvexHull as my
    from sklearn import datasets
    valid = False
    data = None
    print("Pilih sumber dari data yang ingin Anda masukkan(dalam angka): ")
    print("1.Dataset sklearn")
    print("2.CSV")
    sumber_data = int(input("Masukkan pilihan Anda: "))
    if(sumber_data==1):
        while(not valid):
            print("Pilih dataset yang diinginkan: ")
            print("1.iris")
            print("2.digits")
            print("3.wine")
            print("4.breast cancer")
            pilihan = int(input("Masukkan pilihan Anda(dalam angka): "))
            if(pilihan==1):
                data = datasets.load_iris()
                valid = True
            elif(pilihan==2):
                data = datasets.load_digits()
                valid = True
            elif(pilihan==3):
                data = datasets.load_wine()
                valid = True
            elif(pilihan==4):
                data = datasets.load_breast_cancer()
                valid = True
            else:
                print("Pilihan Tidak Valid!")
                
    elif(sumber_data==2):
        nama = input("Masukkan nama file(tanpa perlu menuliskan .csv) yang berada di folder test: ")
        data = pd.read_csv("../test/"+nama+".csv")
        valid = True
    else:
        print("Pilihan tidak valid!\nKeluar program...")
    if(valid):
        df = pd.DataFrame(data.data, columns=data.feature_names)
        df['Target'] = pd.DataFrame(data.target)
        print("Dimensi data: ",df.shape)
        df.head()

        #visualisasi hasil ConvexHull
        plt.figure(figsize = (10, 6))
        sumbu_x,sumbu_y = getAxis(df)
        columns_list = df.columns.values.tolist()
        plt.title(columns_list[sumbu_y]+" vs "+columns_list[sumbu_x])
        plt.xlabel(columns_list[sumbu_x])
        plt.ylabel(columns_list[sumbu_y])
        #Asumsi ada atribut target_names
        for i in range(len(data.target_names)):
            bucket = df[df['Target'] == i]
            bucket = bucket.iloc[:,[sumbu_x,sumbu_y]].values
            hull = my.MyConvexHull(bucket)
            plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i],c=hull.color)
            for simplex in hull.simplices:
                plt.plot(bucket[simplex, 0], bucket[simplex, 1], hull.color)
        plt.legend()
        plt.show() 