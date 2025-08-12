class HotelReservationSystem:
    def __init__(self, rooms_file, reservations_file):
        self.rooms = {}
        self.reservations = {}
        self.load_rooms(rooms_file)
        self.load_reservations(reservations_file)

    def load_rooms(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                room_type, room_number = line.strip().split()
                if room_type not in self.rooms:
                    self.rooms[room_type] = []
                self.rooms[room_type].append(room_number)

    def load_reservations(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                room_number, guest_name = line.strip().split(maxsplit=1)
                self.reservations[room_number] = guest_name

    def save_reservations(self, file_path):
        with open(file_path, 'w') as file:
            for room_number, guest_name in self.reservations.items():
                file.write(f"{room_number} {guest_name}\n")

    def check_availability(self, room_type):
        available_rooms = [room for room in self.rooms.get(room_type, []) if room not in self.reservations]
        return available_rooms

    def book_room(self, room_type, room_number, guest_name):
        if room_number in self.reservations:
            return f"Oda zaten rezerve edilmiş: {room_number}"
        self.reservations[room_number] = guest_name
        self.save_reservations("reservations.txt")
        return f"Rezervasyon yapıldı: {room_number} ({guest_name})"

    def cancel_reservation(self, room_number):
        if room_number in self.reservations:
            guest_name = self.reservations.pop(room_number)
            self.save_reservations("reservations.txt")
            return f"Rezervasyon iptal edildi: {room_number} ({guest_name})"
        return f"Bu oda rezerve edilmemiş: {room_number}"

    def show_status(self):
        for room_type, room_numbers in self.rooms.items():
            available_count = len(self.check_availability(room_type))
            booked_count = 100 - available_count
            print(f"{room_type} Odaları - Dolu: {booked_count}, Boş: {available_count}")

    def show_reservations(self):
        for room_number, guest_name in self.reservations.items():
            print(f"Oda: {room_number}, Misafir: {guest_name}")


def main():
    rooms_file = "rooms.txt"
    reservations_file = "reservations.txt"
    hotel_system = HotelReservationSystem(rooms_file, reservations_file)

    while True:
        print("\n-- OTEL REZERVASYON SİSTEMİ --")
        print("1. Odaları Göster")
        print("2. Rezervasyon Yap")
        print("3. Rezervasyon İptal")
        print("4. Rezervasyon Durumu Göster")
        print("5. Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            room_type = input("Oda tipini seçin (EKO, VIP, LÜKS, YILDIZ): ")
            available_rooms = hotel_system.check_availability(room_type)
            print(f"{room_type} odalarında şu an {len(available_rooms)} boş oda bulunmaktadır.")

        elif choice == "2":
            room_type = input("Oda tipini seçin (EKO, VIP, LÜKS, YILDIZ): ")
            available_rooms = hotel_system.check_availability(room_type)
            if available_rooms:
                room_number = available_rooms[0]
                guest_name = input("Misafir adını girin: ")
                print(hotel_system.book_room(room_type, room_number, guest_name))
            else:
                print("Üzgünüz, seçtiğiniz türde boş oda bulunmamaktadır.")

        elif choice == "3":
            room_number = input("İptal edilecek oda numarasını girin: ")
            print(hotel_system.cancel_reservation(room_number))

        elif choice == "4":
            hotel_system.show_status()
            hotel_system.show_reservations()

        elif choice == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
