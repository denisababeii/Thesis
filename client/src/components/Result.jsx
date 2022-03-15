const [data, setData] = useState([{}])

useEffect(() => {
    fetch("/result").then(
        res => res.json()
    ).then(
        data => {
            setData(data)
            console.log(data)
        }
    )
}, [])

return (
    <div>
        {(typeof data.result === 'undefined') ? (
            <p>Loading...</p>
        ): ( 
            data.result.map((item, i) => (
                <p key={i}>{item.map((subitem, j) => (
                    <div>{subitem}</div>
                )
                )}</p>
            ))
        )}
    </div>
)