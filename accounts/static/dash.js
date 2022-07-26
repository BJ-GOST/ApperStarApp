var JobProgress = document.getElementById('job-progress')
var progress = JobProgress.dataset.progress 
var undone = 100 - progress


var xValues = ["Done", "Undone"];
var yValues = [progress, undone];
var options = {        
    cutout: 40
};

var barColors = [
  "gold",
  "linen",
];

new Chart("myChart", {
  type: "doughnut",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    cutoutPercentage: 70,
    responsive: true,
    maintainAspectRatio: false,
    title: {
      display: true,
      text: "Job progress:" + ' ' + progress + '%'
    },
  }
});