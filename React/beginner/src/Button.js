import PropTypes from "prop-types"
import style from './button.module.css'

function Button ({text}) {
    return <button  className={style.btn}> {text} </button>
}

Button.propTypes = {
    text: PropTypes.string.isRequired,
}

export default Button;