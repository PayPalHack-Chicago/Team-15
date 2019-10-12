const annualInflationRate = 0.02    // 2%
const annualInterestRate = 0.00     // 10%
const meanRetirementAge = 66        // 66 years
const meanStartingAge = 21          // 21 years

const jobToEarningsTimeline = require("./input/job-to-earnings-timeline.json")
const pretaxIncomeToPostTaxSavingData = require("./input/pretax-income-to-posttax-saving-portion.json")

function pretaxIncomeAmountToPostTaxSavingAmount(pretaxIncome) {
    for (var j = 0; j < pretaxIncomeToPostTaxSavingData.quantileBounds.length; j++) {
        if (pretaxIncome >= pretaxIncomeToPostTaxSavingData.quantileBounds[j][0] && pretaxIncome <= pretaxIncomeToPostTaxSavingData.quantileBounds[j][1]) {
            break
        }
    }

    // "quantileBounds": [
    //     [ 0,     24638  ],
    //     [ 24638, 47110  ],
    //     [ 47110, 77552  ],
    //     [ 77552, 126855 ],
    //     [ 126855, 1E10  ]
    // ],
    // "quantileData": {
    //     "0": {
    //         "totalIncome": 25525,
    //         "savingPortion": 0
    //     },
    //     "1": {
    //         "totalIncome": 37319,
    //         "savingPortion": 0
    //     },
    //     "2": {
    //         "totalIncome": 52431,
    //         "savingPortion": 0.055215426
    //     },
    //     "3": {
    //         "totalIncome": 86363,
    //         "savingPortion": 0.199796209
    //     },
    //     "4": {
    //         "totalIncome": 188102,
    //         "savingPortion": 0.265095533
    //     }
    // }


    // let slope = 0
    // let offset = 0
    // let dx = 0

    // // special case on the left
    // if (pretaxIncome < 24638) {
    //     slope = 0
    //     offset = 0
    //     dx = 0
    // } else if (pretaxIncome < (24638 + 47110) / 2) {
    //     slope = 0
    //     offset = 24638
    //     dx = ((24638  + 47110) / 2) - pretaxIncome
    // } else if (pretaxIncome < 47110) {
    //     slope = (0.055215426 / )

    // } else if (pretaxIncome < (47110 + 0.5*(77552 - 47110))) {
    
    // } else if (pretaxIncome < 77552) {
        
    // } else if (pretaxIncome < 77552 + 0.5*(126855 - 77552)) {

    // } else if (pretaxIncome < 126855) {

    // } else {

    // }

    // return offset + (slope * dx)

    return pretaxIncomeToPostTaxSavingData.quantileData[j].savingPortion * pretaxIncome
}

function getJobEarningsAtYear(jobName, yearsAfterInitialHire) {
    const length = Object.keys(jobToEarningsTimeline[jobName]).length
    return jobToEarningsTimeline[jobName][Math.min(yearsAfterInitialHire, length)]

    // return (
    //     jobToEarningsTimeline[jobName][length - 1] +
    //     (
    //         jobToEarningsTimeline[jobName][length - 2] - 
    //         jobToEarningsTimeline[jobName][length - 1]
    //     ) * (
    //         yearsAfterInitialHire - (length - 1)
    //     )
    // )
}

const wealthTimelines = {}

for (var jobName in jobToEarningsTimeline) {
    // console.log("Processing", jobName)

    wealthTimelines[jobName] = [ getJobEarningsAtYear(jobName, 1) ]

    for (var j = 2; j < meanRetirementAge - meanStartingAge; j++) {
        wealthTimelines[jobName][j - 1] = (
            (1 + annualInterestRate) * wealthTimelines[jobName][j - 2] + 
            pretaxIncomeAmountToPostTaxSavingAmount(getJobEarningsAtYear(jobName, j))
        )
    }

    // console.log(jobName, "=>", wealthTimelines[jobName].length)
    
    for (var j = 0; j < wealthTimelines[jobName].length; j++) {
        wealthTimelines[jobName][j] *= Math.pow(1 - annualInflationRate, j)
    }
}

let csv = `Year,${Object.keys(wealthTimelines).map(s => `"${s}"`).join(",")}\n`

for (var j = 0; j < meanRetirementAge - meanStartingAge - 1; ++j) {
    csv += `${j}`
    for (var jobName in wealthTimelines) {
        csv += `,${wealthTimelines[jobName][j]}`
    }
    csv += `\n`
}

console.log(csv)