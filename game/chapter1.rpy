label chapter1:
    #Chapter 1

    #scene CG_chapter1_1 with Fade (0.0, 1, 1.0)

    #play sound embusan angin

    show Elizabeth base

    Elizabeth "Dingin sekali…"

    Elizabeth "(Aku selalu tidak beruntung. Kondisiku yang melemah serta diriku yang selalu sensitif dengan cuaca dingin seperti ini sejak kecil. 
    Namun, apa boleh buat. Aku tinggal di benua yang seperti ini)"

    Elizabeth "Beberapa hari kemarin, rasa dingin datang dari tulang punggungku. Aku merasakan sensasi yang mengundang rasa takut dan merinding. 
    Bahkan, rasa dingin pun menjadi masalah yang besar. Rasanya seperti ada yang mengawasiku."

    hide Elizabeth

    #scene  BG raung kantor with Fade (0.0, 1, 1.0)

    show Elizabeth bosan with dissolve:
        #Ditengah
        xalign 0.5

    Elizabeth "… Huft, kasus-kasus ini terus saja bermunculan, tidak ada habisnya."

    Elizabeth "(Akhir-akhir ini banyak permintaan untuk menyelidiki kasus mengenai barang peninggalan atau anak yang hilang.)"

    Elizabeth "(Lokasinya pun hanya di sekitar daerah ini)"

    show Elizabeth kesal:
        #ditengah
        xalign 0.5

    Elizabeth "(Membosankan sekali. Tidak ada satupun kasus yang cocok untukku.)"

    show Elizabeth bosan:
        #Ditengah
        xalign 0.5

    Elizabeth "(Semuanya terlalu sederhana.)"

    Elizabeth "(Akan lebih baik jika kasusnya sedikit, namun sulit dipecahkan…)"

    #play sound SFX ketok pintu
    #play sound SFX buka pintu

    show Elizabeth base:
        #dikanan
        xalign 0.5
        yalign 0.8

    show Alexander base:
        #ini Tersenyum
        #dikiri
        xalign 0.5
        yalign 0.2

    Alexander "Elizabeth, aku membawakan kopi untuk menemani tugas malammu."

    Elizabeth "… Ya, letakkan saja di meja."

    Alexander "..."

    show Elizabeth bingung:
        xalign 0.5
        yalign 0.8

    Elizabeth "Kenapa kamu senyum-senyum sendiri seperti monyet yang kerasukan? Aneh sekali. 
    Tidak seperti dirimu yang biasanya."

    Alexander "Ah, tidak. Aku hanya berpikir Elizabeth yang sedang 
    bekerja dengan serius terlihat manis."

    show Elizabeth bosan:
        xalign 0.5
        yalign 0.8

    Elizabeth "Hentikan omong kosongmu dan cepat bantu aku memilah laporan kasus yang akan 
    kita kerjakan nanti."  

    show Alexander normal:
        xalign 0.5
        yalign 0.2

    Alexander "Baik, Nona Elizabeth~"

    Elizabeth "… Huh, sudah 25 tahun aku hidup dan 5 tahun bekerja sebagai detektif, 
    belum ada kasus yang berhasil menarik minatku."

    Alexander "Mungkin suatu saat kamu akan menemukannya."

    show Alexander tegas:
        xalign 0.5
        yalign 0.2

    Alexander "… Tapi tidak sekarang."

    show Elizabeth bosan:
        xalign 0.5
        yalign 0.8

    Elizabeth "Barusan kamu mengatakan sesuatu?"

    show Alexander base:
        xalign 0.5
        yalign 0.2

    Alexander "Tidak, kok. Aku hanya mengatakan nona Elizabeth sangat menekuni pekerjaannya dan 
    aku kagum dengan sisimu yang seperti itu."

    show Elizabeth kesal:
        xalign 0.5
        yalign 0.8

    Elizabeth "Kelihatannya kamu senang sekali mengeluarkan omong kosong dari mulut madumu."

    show Elizabeth sarkas:
        xalign 0.5
        yalign 0.8

    Elizabeth "Pantas saja kamu populer di kalangan wanita."

    show Alexander malu:
        xalign 0.5
        yalign 0.2

    Alexander "Ahaha, apakah benar? "

    show Elizabeth bingung:
        xalign 0.5
        yalign 0.8
    
    Elizabeth "… kamu ternyata lemah dengan pujian, ya."

    show Alexander terkejut:
        xalign 0.5
        yalign 0.2

    Alexander "B-bukan begitu. Lagipula ada satu wanita yang belum tertarik dengan—"

    #play sound suara_menghantam_kejendela

    hide Alexander #and Elizabeth

    hide Elizabeth

    #scene CG_chapter1_3 with Fate(0.0, 1, 1.0)
    
    Alexander "Wah, a[a itu tadi!?"

    Alexander "…Kupikir ada burung yang menabrak jendela."

    Elizabeth "Imajinasimu masih sama seperti dulu."

    Alexander "Haha, aku bingung harus menganggap itu pujian atau hinaan…"

    Elizabeth "Sudahlah, fokus kembali pada pekerjaanmu."

    Alexander "Baik, Nona~"

    #scene Ruang_kantor with Dissolve(1, alpha = False)
    #Dissolve(time, alpha=False, time_warp=None, **properties)

    "Waktu berlalu diisi dengan keheningan, hanya suara kertas bergesekan yang memenuhi seisi ruangan."

    #play sound suara_besi

    show Alexander base:
        yalign 0,5
        xalign 0.2
    
    Alexander "Oh, sepertinya ada pesan baru. Saya ambilkan dulu ya."

    hide Alexander

    show Elizabeth bosan:
        yalign 0.5
        xalign 0.2
    
    Elizabeth "Lakukanlah sebebasmu."

    #play sound berjalan_dikayu

    Alexander "Mari kita lihat apa yang kita dapat hari ini…"

    Alexander "Hm… sepertinya banyak dari kasus ini yang sering kejadian disini, tapi tidak bisa dibantu secara langsung."

    #ATL item surat

    Alexander "Eh? Surat ini…"

    Alexander "Dari semua yang didapat, hanya ini yang terlihat kuno. Apakah ini tertimbun dengan yang lainnya?"

    #ATL item out

    Alexander "Alexander: Apa boleh buatlah! Setidaknya bisa saja ada kasus menarik nantinya."

    #play sound berja;an_dikayu

    Alexander "Banyak juga ternyata pengiriman surat hari ini!"

    Elizabeth "Tapi semuanya hanya hal-hal biasa, kan?"

    Alexander "Ahaha… ternyata mudah ditebak ya?"

    Elizabeth "Mau mencoba pikirkan apa lagi, selain menunggu kasus yang menarik?"

    Alexander "Hmm… omong-omong tentang menarik, aku menemukan surat kuno diantara mereka."

    Elizabeth "Surat kuno?"

    Alexander "Iya, surat yang ini."

    #ATL item surat

    show Elizabeth terkejut

    Elizabeth "…!"

    Alexander "Tinta tulisannya sudah mulai menghilang jadi susah tahu dari siapa menuju siapa."

    Alexander "Belum lagi betapa rusaknya kertas surat ini!"

    #ATL item out

    #Ada Tulisan "Pada waktu malam, sebuah anak akan menghilang tanpa jejak. Keluarlah dan bertemu di tempat pengumpulan antik, dimana mereka segera terlupakan."

    Elizabeth "(Surat ini… saya tidak tahu kenapa Alexander tidak melihat ini, tapi…)"

    Elizabeth "(Sepertinya kasus yang menarik telah datang.)"

    Alexander "-Jadi seperti itulah. Saya akan membakarnya terlebih dahu-"

    Elizabeth "Apa yang kau lakukan, Alexander?!"

    Alexander "Eh?"

    Elizabeth "Apa kau benar-benar lupa? Peraturan utama untuk kasus, selalu menerima surat meskipun berbagai macam masalah…"

    #Play sound kresek

    Elizabeth "…Terutama yang berbeda dengan yang lain, baik secara bentuk maupun permohonan."

    Alexander "Oh… oh, tentu saja! Bagaimana saya lupa itu?!"

    Elizabeth "Karena kau lebih memusingkan orang lain daripada diri sendiri."

    Alexander "M…Mhm…"

    Elizabeth "Oleh karena itu, saya akan bepergian sementara untuk bertemu dengan klien dari surat ini."

    show Alexander normal

    Alexander "Ah, oke. Apa perlu kuteman—"

    show Elizabeth kesal

    Elizabeth "Jangan lanjutkan ucapanmu atau buku di atas meja ini akan melayang ke kepalamu."

    Alexander "Siap laksanakan, Nona!"

    #scene CG_chapter1_4 with Fade(0, 1, 1.0)

    #play music lagu_mencekam

    Elizabeth "Keluarlah. Aku tahu kamu yang mengirimkan surat ini."

    Hantu "Tolong … selamatkan anak itu …"

    Elizabeth "Argh, kamu benar-benar membuatku frustasi."

    Elizabeth "Memangnya kenapa aku harus membantu anak itu?"

    Hantu "Kumohon… dia bisa… mati…"

    Elizabeth "…?"

    Elizabeth "Seberapa berbahaya kasus ini sampai merenggut nyawa orang…"

    Hantu "Kasus ini… bisa menjadi kasus yang menarik… untukmu…"

    Elizabeth "!!!"

    Elizabeth "Sial, kamu menguping pembicaraanku."

    Elizabeth "Huft, baiklah. Tapi tidak gratis, lho."

    Hantu "Pecahan… jiwa…"

    Elizabeth "Kamu serius?"

    Hantu "… Serius…"

    Hantu "Setelah kasus selesai… aku akan… memberikannya… untukmu…"

    Elizabeth "Hm, oke."

    Elizabeth "Aku membutuhkan keterangan lebih lanjut mengenai identitas anak ini dan tempat terakhir kamu melihatnya."

    Hantu "William.. umur 10 tahun… laki-laki… memakai syal berwarna biru laut… terakhir ada di … perbatasan kota …"

    Elizabeth "Hm, perbatasan kota, ya? Baiklah."

    Hantu "… terima … kasih …"

    scene Ruang_kantor with Dissolve (1, alpa = False)

    show Elizabeth

    Elizabeth "Alex, persiapkan alat-alat untuk penyelidikan besok. Kita mendapatkan tugas penting untuk diselesaikan."

    Alexander "H-hah? Tiba-tiba sekali… Baik akan kupersiapkan…"

    Alexander "Kira-kira kasus apa yang akan kita kerjakan besok?"

    Elizabeth "Kasus ‘istimewa’, anak hilang."

    #END Chapter 1

    return