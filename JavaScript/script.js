/**
 * @type {Object}
 */
let customer = {
    name: "Johnny Johnson",
    birthDate: "1985-07-15",
    gender: "Male",
    roomPreferences: ["No Smoking", "Ground floor"],
    paymentMethod: "Debit Card",
    mailingAddress: {
        street: "456 Elm Street",
        city: "Springfield",
        state: "IL",
        postalCode: "90210",
        country: "USA"
    },
    phoneNumber: "312-555-7890",
    stayPeriod: {
        checkIn: "2024-08-01",
        checkOut: "2024-08-07"
    },
    
    getAge: function() {
        let today = new Date();
        let birthDate = new Date(this.birthDate);
        let age = today.getFullYear() - birthDate.getFullYear();
        let monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        return age;
    },
    
    getStayDuration: function() {
        let checkInDate = new Date(this.stayPeriod.checkIn);
        let checkOutDate = new Date(this.stayPeriod.checkOut);
        let timeDiff = checkOutDate - checkInDate;
        let daysDiff = timeDiff / (1000 * 3600 * 24);
        return daysDiff;
    },

    getDescription: function() {
        return `
            <p>Our guest, <strong>${this.name}</strong>, aged ${this.getAge()} years, is staying with us from ${this.stayPeriod.checkIn} to ${this.stayPeriod.checkOut}, which is a total of ${this.getStayDuration()} days.</p>
            <p>${this.gender} prefers a ${this.roomPreferences.join(", ")} room and has chosen to pay with a ${this.paymentMethod}. You can reach ${this.name} at ${this.phoneNumber}.</p>
            <p>${this.name} resides at ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}, ${this.mailingAddress.postalCode}, ${this.mailingAddress.country}.</p>
        `;
    }
};

document.getElementById('guest-description').innerHTML = customer.getDescription();
