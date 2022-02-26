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
                    text: "area", // todo: more general name/make it changeable per mission in the config
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
                    text: "price", // todo: more general name/make it changeable per mission in the config
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
                text: "housing", // todo: more general name/make it changeable per mission in the config
                font: {
                    size: 20
                }
            }
        }
    }
};
