export let HousingChartConfig = {
    data: {
        datasets: [{
            type: "scatter",
            data: null,
            backgroundColor: 'rgb(61,57,57)'
        }, {
            type: "line",
            data: null,
            backgroundColor: 'rgb(91,204,204)'
        }],
    },
    options: {
        animation: false,
        responsive: true,
        scales: {
            x: {
                display: true,
                title: {
                    display: true,
                    text: "price",
                    color: 'rgb(0,0,0)',
                    font: {
                        size: 15
                    }
                }
            },
            y: {
                display: true,
                title: {
                    display: true,
                    text: "area",
                    color: 'rgb(0,0,0)',
                    font: {
                        size: 15
                    }
                }
            }
        },
        plugins: {
            legend: {
                display: false
            },
            title: {
                display: true,
                text: "housing",
                font: {
                    size: 20
                }
            }
        }
    }
};
