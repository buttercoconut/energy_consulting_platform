<template>
  <div class="energy-dashboard">
    <h2>Energy Consumption Dashboard</h2>
    <canvas id="energyChart"></canvas>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

const chartRef = ref<HTMLCanvasElement | null>(null);

async function fetchData() {
  // Replace with real API endpoint
  const res = await fetch('/api/energy?building_id=1&start=2024-01-01T00:00:00Z&end=2024-01-07T23:59:59Z');
  const data = await res.json();
  return data.items;
}

onMounted(async () => {
  const data = await fetchData();
  const labels = data.map((d: any) => d.timestamp);
  const values = data.map((d: any) => d.energy_kwh);

  if (chartRef.value) {
    new Chart(chartRef.value, {
      type: 'line',
      data: {
        labels,
        datasets: [
          {
            label: 'Energy (kWh)',
            data: values,
            borderColor: 'rgba(75,192,192,1)',
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        scales: {
          x: { display: true, title: { display: true, text: 'Timestamp' } },
          y: { display: true, title: { display: true, text: 'kWh' } },
        },
      },
    });
  }
});
</script>

<style scoped>
.energy-dashboard {
  max-width: 800px;
  margin: 0 auto;
}
</style>
