# Define characters
define p = Character("Paijo", color="#77ff77")
define j = Character("Joko", color="#c9982f")
define d_uji = Character("Penguji", color="#ff3d3d")
define d_bim = Character("Pembimbing", color="#2f72c9")
define n = Character(None, kind=nvl)

# Variable to track if it's a cutscene or interactive gameplay
default in_cutscene = False
default time_stop = False

# Exploration specific flags
default current_location = "kos"  # Start in dorm room
define locations = {
    "kos": {
        "explorable": ["dapur"],
        "name": "Kos",
    },
    "dapur": {
        "explorable": ["kos"],
        "name": "Dapur",
    },
}

define bidang_ilmu = {
    "KCV": {
        "nama": "Komputasi Cerdas dan Visi",
        "deskripsi": "memanipulasi dan menganalisis data citra pada berbagai bidang aplikasi, kemampuan menerapkan metode sistem cerdas pada berbagai bidang aplikasi dan kemampuan memodelkan dan mengoptimasikan sistem nyata.",
        "mata_kuliah": [
            "Pengolahan Citra Digital",
            "Analisis Data Multivariat",
            "Data Mining",
            "Komputasi Biomedik",
            "Visi Komputer",
            "Sistem Temu Kembali Informasi",
            "Robotika",
            "Analisis Media Sosial dan Topik Khusus KCV"
        ]
    },
    "AlPro": {
        "nama": "Algoritma dan Pemrograman",
        "deskripsi": "merancang dan menganalisa algoritma dalam menyelesaikan permasalahan secara efektif dan efisien berdasarkan kaidah pemrograman yang kuat, mampu mengaplikasikan model pemrograman yang mendasari berbagai bahasa pemrograman yang ada, serta mampu memilih bahasa pemrograman untuk menghasilkan aplikasi yang sesuai, seperti mengembangkan sistem/aplikasi berbasis kerangka kerja dan pada perangkat bergerak.",
        "mata_kuliah": [
            "Pengembangan Analisis Algoritma",
            "Pemrograman Berbasis Antarmuka",
            "Pemorgraman Perangkat Bergerak",
            "Topik Khusus Algroritma dan Pemrograman"
        ]
    },
    "GIGA": {
        "nama": "Grafika, Interaksi, Gim, dan Analitik",
        "deskripsi": "mendesain, mengembangkan dan mendokumentasikan proses pembuatan game sesuai dengan standar. Serta membuat model 3 dimensi dan pemograman di dalam realitas virtual serta aplikasi realitas virtual 3 dimensi dengan menggunakan game engine.",
        "mata_kuliah": [
            "Animasi Komputer dan Permodelan 3D",
            "Desain Pengalaman Pengguna",
            "Game Cerdas",
            "Game Edukasi dan Simulasi",
            "Game Engine",
            "Teknik Pengembangan Game",
            "Grafika Komputer",
            "Interaksi Manusia dan Komputer",
            "Realitas X",
            "Topik Khusus GIGA"
        ]
    },
    "RPL": {
        "nama": "Rekayasa Perangkat Lunak",
        "deskripsi": "melakukan pengujian perangkat lunak, Kemampuan mengelola proyek perangkat lunak, Kemampuan mengurangi resiko kesalahan perangkat lunak, dan Kemampuan membuat perangkat lunak game.",
        "mata_kuliah": [
            "Penjaminan Mutu Perangkat Lunak",
            "Arsitektur Perangkat Lunak",
            "Evolusi Perangkat Lunak",
            "Konstruksi Perangkat Lunak",
            "Penyempurnaan Proses Perangkat Lunak",
            "Ekonomi Rekayasa Perangkat Lunak",
            "Topik Khusus RPL"
        ]
    },
    "KBJ": {
        "nama": "Komputasi Berbasis Jaringan",
        "deskripsi": "membangun infrastruktur jaringan yang aman, kemampuan membangun sistem grid, Kemampuan membangun aplikasi jaringan sesuai Standard dan Kemampuan membangun aplikasi multimedia berbasis jaringan.",
        "mata_kuliah": [
            "Komputasi Bergerak",
            "Sistem Terdistribusi",
            "Keamanan Informasi dan Jaringan",
            "Jaringan Multimedia",
            "Komputasi Awan",
            "Forensik Digital",
            "Komputasi Pervasif dan Jaringan Sensor",
            "Topik Khusus Komputasi berbasis Jaringan"
        ]
    },
    "Netics": {
        "nama": "Teknologi Jaringan dan Keamanan Siber Cerdas",
        "deskripsi": "membangun berbagai macam arsitektur jaringan sesuai standar teknologi terkini dan menerapkan keamanan jaringan.",
        "mata_kuliah": [
            "Sistem Operasi",
            "Jaringan Komputer",
            "Pemrograman Jaringan",
            "Jaringan Nirkabel",
            "Teknologi Antar Jaringan",
            "Perancangan Keamanan Sistem Dan Jaringan",
            "Desain dan Audit Jaringan",
            "Teknologi IoT",
            "Topik Khusus Teknologi Jaringan dan Keamanan Siber Cerdas"
        ]
    },
    "MCI": {
        "nama": "Manajemen Cerdas Informasi",
        "deskripsi": "menganalisis, mensintesa dan mengevaluasi proses bisnis dan sistem informasi pada sistem Enterprise, mengimplementasikan rekayasa pengetahuan ke dalam suatu aplikasi, melakukan investigasi, pengujian, evaluasi kematangan dan kepatutan terhadap prosedur standard dan tata kelola teknologi informasi, melakukan tata kelola proyek dan sumber daya manusia dan merancang dan mengimplementasikan solusi basis data terdistribusi dan teknologi Big Data.",
        "mata_kuliah": [
            "Sistem Enterprise",
            "Rekayasa Pengetahuan",
            "Sistem Informasi Geografis",
            "Audit Sistem",
            "Tata Kelola Teknologi Informasi",
            "Basis Data Terdistribusi",
            "Big Data",
            "Topik Khusus Manajemen Informasi"
        ]
    },
    "PKT": {
        "nama": "Permodelan dan Komputasi Terapan",
        "deskripsi": "riset dan kerjasama industri di bidang pemodelan & simulasi, peramalan sains, optimasi, serta komputasional saintifik.",
        "mata_kuliah": [
            "Pemodelan dan Simulasi",
            "Matematika Diskrit",
            "Teori Graf dan Otomata",
            "Aljabar Linear dan Matriks",
            "Probabilitas dan Statistika",
            "Komputasi Numerik",
            "Riset Operasi",
            "Analisis Data Multivariat",
            "Topik Khusus Permodelan dan Komputasi Terapan"
        ]
    },
    # Add more fields as needed
}

# Helper functions
init python:
    def move_to_map(location_label):
        store.time_stop = True
        store.show_map = False
        renpy.transition(fade)
        renpy.jump(location_label)
    # def interact_environment(env_label):
    #     store.can_move_places = 0
    #     renpy.call(env_label)
    def format_duration(minutes):
        hours = minutes // 60
        mins = minutes % 60
        return "{} jam {} menit".format(hours, mins)
    def fade_music_transition(new_track=None, fade_out=1.0, fade_in=0.0, music_volume=1.0, mode=None):
        """
        Fades out current music, stops it, and optionally plays a new track with fade in.
        
        Parameters:
        - new_track: The music track to play after fading out (None to just stop current music)
        - fade_out: Time in seconds to fade out current music
        - fade_in: Time in seconds to fade in new music (0 for immediate)
        - music_volume: Target volume for new music (default 1.0)
        - mode: The mode for the transition (e.g., 'cutscene', 'normal'), can be used to adjust fade times or volumes based on context
        Example usage: fade_music_transition('songname.ogg', fade_out=2.0, fade_in=1.0)
        """
        if new_track:
            renpy.music.set_volume(volume=0.0, delay=fade_out, channel='music')
            if mode == 'cutscene':
                renpy.pause(fade_out)
            renpy.music.stop(channel='music')
            renpy.music.set_volume(volume=music_volume, delay=fade_in, channel='music')
            renpy.music.play(new_track, channel='music', fadein=fade_in)

    def fade_stop_music(fade_out=1.0, mode=None):
        """
        Fades out current music, stops it, and optionally plays a new track with fade in.
        
        Parameters:
        - new_track: The music track to play after fading out (None to just stop current music)
        - fade_out: Time in seconds to fade out current music
        - fade_in: Time in seconds to fade in new music (0 for immediate)
        - music_volume: Target volume for new music (default 1.0)
        - mode: The mode for the transition (e.g., 'cutscene', 'normal'), can be used to adjust fade times or volumes based on context
        Example usage: fade_music_transition('songname.ogg', fade_out=2.0, fade_in=1.0)
        """
        renpy.music.set_volume(volume=0.0, delay=fade_out, channel='music')
        if mode == 'cutscene':
            renpy.pause(fade_out)
        renpy.music.stop(channel='music')
        renpy.music.set_volume(volume=1.0, delay=0, channel='music')

    # Hide all screens during cutscenes, show during interactive gameplay
    def set_cutscene_mode(is_cutscene):
        global in_cutscene, show_calendar, show_detailed_stats, time_stop
        in_cutscene = is_cutscene
        time_stop = is_cutscene
        show_calendar = False  # Ensure calendar is hidden during cutscenes
        show_detailed_stats = False  # Ensure detailed stats are hidden during cutscenes
        renpy.retain_after_load()  # Ensure this state persists after loading