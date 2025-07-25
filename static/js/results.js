
document.addEventListener('DOMContentLoaded', () => {

    const calculateBtn = document.getElementById('calculate-btn');
    const sgpaResultDiv = document.getElementById('sgpa-result');
    const sgpaValueSpan = document.getElementById('sgpa-value');
    const remarkText = document.getElementById('sgpa-remark');

    calculateBtn.addEventListener('click', () => {

        const sgpa = parseFloat(sgpaValueSpan.textContent);
        
       
        let remark = '';

        if (sgpa >= 9.0) {
            remark = "Outstanding!";
        } else if (sgpa >= 8.0) {
            remark = "Excellent!";
        } else if (sgpa >= 7.0) {
            remark = "Good Job!";
        } else if (sgpa >= 6.0) {
            remark = "Solid Effort";
        } else {
            remark = "Keep Trying";
        }

        // Apply the determined remark
        remarkText.textContent = remark;

        // Hide the button and show the results container
        calculateBtn.style.display = 'none';
        sgpaResultDiv.style.display = 'block';
    });
});