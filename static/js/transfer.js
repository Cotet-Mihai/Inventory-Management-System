// Adaugam un event listener pentru selectul Source Warehouse
document.getElementById('source_warehouse').addEventListener('change', function() {
    const warehouseId = this.value;
    if (warehouseId) {
        // Facem un fetch catre ruta care returneaza itemele pentru depozitul selectat
        fetch(`/get_items_in_warehouse/${warehouseId}`)
            .then(response => response.json())
            .then(data => {
                const itemSelect = document.getElementById('item');
                itemSelect.innerHTML = '<option value="" disabled selected>Select Item</option>'; // Resetam optiunile
                data.forEach(item => {
                    const option = document.createElement('option');
                    option.value = item.item_id;
                    option.textContent = item.item_name;
                    itemSelect.appendChild(option);
                });
            })
            .catch(error => console.error('Error fetching items:', error)); // Afisam eroarea in caz de esec
    }
});
