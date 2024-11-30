// static/js/create_post.js

document.addEventListener('DOMContentLoaded', function() {
    // Access variables passed from the template
    const paragraphName = window.paragraphName;
    const addAllParagraphsId = window.addAllParagraphsId;

    // Form submission validation
    document.getElementById('create-post-form').addEventListener('submit', function(event) {
        const paragraphCheckboxes = document.querySelectorAll(`input[name="${paragraphName}"]`);
        let isAnyChecked = false;
        paragraphCheckboxes.forEach(function(checkbox) {
            if (checkbox.checked) {
                isAnyChecked = true;
            }
        });
        if (!isAnyChecked) {
            event.preventDefault();
            alert('Please select at least one paragraph');
        }
    });

    // Handle "Select All Paragraphs" checkbox
    const addAllParagraphsField = document.getElementById(addAllParagraphsId);
    const paragraphCheckboxes = document.querySelectorAll(`input[name="${paragraphName}"]`);

    if (addAllParagraphsField && paragraphCheckboxes.length > 0) {
        addAllParagraphsField.addEventListener('change', function() {
            const isChecked = this.checked;
            paragraphCheckboxes.forEach(function(checkbox) {
                checkbox.checked = isChecked;
            });
        });

        // Synchronize "Select All" checkbox with individual checkboxes
        paragraphCheckboxes.forEach(function(checkbox) {
            checkbox.addEventListener('change', function() {
                const allChecked = Array.from(paragraphCheckboxes).every(function(cb) {
                    return cb.checked;
                });
                addAllParagraphsField.checked = allChecked;
            });
        });
    }
});
