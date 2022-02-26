export let HousingChartConfig = {
    data: {
        datasets: [{
            type: "scatter",
            data: null,
            backgroundColor: 'rgb(141,130,130)',
            order: 2
        }, {
            type: "line",
            data: null,
            borderColor: 'rgb(0,0,0)', // the line color
            backgroundColor: 'rgb(0,0,0)',  // the dot color
            order: 1
        }, {
            type: "line",
            data: null,
            borderColor: 'rgb(0,0,0)', // the line color
            backgroundColor: 'rgb(0,0,0)',  // the dot color
            order: 3
        }, {
            type: "line",
            data: null,
            borderColor: 'rgb(0,0,0)', // the line color
            backgroundColor: 'rgb(0,0,0)',  // the dot color
            order: 4
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
