async function verifyCertificate() {
    const serial = document.getElementById("serialNumber").value.trim();
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = "";

    if (!serial) {
        resultDiv.innerHTML = "<p class='error'>Please enter serial number</p>";
        return;
    }

    try {
        const response = await fetch(`/verify-certificate/${serial}`);
        const data = await response.json();

        if (!data.success) {
            resultDiv.innerHTML = `<p class='error'>${data.message}</p>`;
            return;
        }

        const cert = data.data;

        resultDiv.innerHTML = `
            <p class="success"><strong>Certificate Valid ✅</strong></p>
            <p><strong>Name:</strong> ${cert.student_name}</p>
            <p><strong>Course:</strong> ${cert.course}</p>
            <p><strong>Year:</strong> ${cert.year}</p>
            <p><strong>Status:</strong> ${cert.status}</p>
        `;
    } catch (err) {
        resultDiv.innerHTML = "<p class='error'>Server error. Try again.</p>";
    }
}
