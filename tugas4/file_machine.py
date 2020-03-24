from control_file import Direct
import json
import logging
import base64

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
COMMAND *space* PARAMETER *space* PARAMETER

FITUR

1. Upload File
   mengupload file ke folder 'file'
   Request   : upload
   Parameter : namafile *spasi* isifile
   Response  : jika berhasil -> ok
               jika gagal    -> error

2. List File
   melihat list file di dalam folder 'file'
   Request   : list
   Parameter : -
   Response  : list file yang ada dalam folder 'file'

3. Download File
   mendownload file berdasarkan nama file
   Request   : download
   Parameter : namafile yang ingin didownload
   Response  : hasil download file

4. Jika command tidak dikenali akan merespon dengan ERRCMD

'''

p = Direct()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                nama = cstring[1].strip()
                file = cstring[2].strip()

                print(nama)
                print(file.encode())
                p.upload_file(nama,file.encode())
                print(nama)
                return "File Berhasil Diunggah"

            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_file()
                dict = {"status":"succes","data":hasil}
                return json.dumps(dict)

            elif (command=='unduh'):
                logging.warning("unduh")
                nama = cstring[1].strip()
                hasil = p.download_file(nama)
                return hasil[0]

            else:
                return "ERRCMD"

        except:
            return "ERROR"

if __name__=='__main__':
    machine = FileMachine()
    input = "pesan.txt"
    hasil = machine.proses("list")
    print(hasil)