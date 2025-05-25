# Control de versions

## ✅ Checklist SemVer + Tags

### 1. 🧪 Antes de versionar

- [ ] Todo el código fue **probado y funciona correctamente**
- [ ] Todos los **tests pasan**
- [ ] El proyecto está en un estado **estable o importante** (lanzamiento, demo, entrega, etc.)

---

### 2. 📄 Decide la nueva versión

- ¿Rompiste compatibilidad con versiones anteriores? → **Incrementa `MAJOR`**
- ¿Añadiste nuevas funcionalidades compatibles? → **Incrementa `MINOR`**
- ¿Solo corregiste errores o hiciste mejoras menores? → **Incrementa `PATCH`**

> 🧠 Ejemplo:  
> Si la versión actual es `v1.2.3` y corriges un bug, la nueva sería `v1.2.4`.

```bash
git tag -a v1.0.0 -m "Release: versión inicial"
git push origin v1.0.0

```