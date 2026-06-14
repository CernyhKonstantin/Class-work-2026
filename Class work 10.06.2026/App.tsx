import './App.css'
import type { CardType } from './types/CardType'

function App() {

  const cards: CardType[] = [
    {
      title: "React Basics",
      description: "Вступ до React та створення компонентів.",
      views: 1200,
      is_show: true,
    },
    {
      title: "TypeScript Fundamentals",
      description: "Основи роботи з типами в TypeScript.",
      views: 980,
      is_show: true,
    },
    {
      title: "Bootstrap Layout",
      description: "Створення адаптивних макетів за допомогою Bootstrap.",
      views: 750,
      is_show: false,
    },
    {
      title: "Django REST API",
      description: "Розробка REST API на Django REST Framework.",
      views: 1500,
      is_show: true,
    },
    {
      title: "Python for Data Analysis",
      description: "Обробка та аналіз даних за допомогою Python.",
      views: 2100,
      is_show: false,
    },
  ]

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>

      <h2>Cards Table</h2>

      <table border={1} cellPadding={10}>
        <thead>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Views</th>
            <th>Is_show</th>
          </tr>
        </thead>

        <tbody>
          {cards.map((card, index) => (
            <tr key={index}>
              <td>{card.title}</td>
              <td>{card.description}</td>
              <td>{card.views}</td>
              <td>{card.is_show ? "Yes" : "No"}</td>
            </tr>
          ))}
        </tbody>

      </table>

    </div>
  )
}

export default App