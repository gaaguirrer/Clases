# Flujo Git — Sparse Checkout

## Inicialización

```bash
cd "C:\Users\ingga\OneDrive\Documentos\Nueva carpeta\Clases"
git init
git remote add origin https://github.com/gaaguirrer/Clases
git config core.sparseCheckout true
git config core.sparseCheckoutCone false
```

Escribir en `.git\info\sparse-checkout` las carpetas deseadas con `/**` al final:

```
Administración de Sistemas de Información/**
Gerencia de Operaciones I/**
Sistemas electrónicos/**
Ingeniería del Software I/**
Libre I (SPSS)/**
Marketing Digital/**
Diseño de Bases de Datos/**
Ingeniería del software III/**
Gestión de Proyectos Tecnológicos/**
Optativa profesional II (gobernanza y Criptografía)/**
```

Luego:
```bash
git clone --sparse --filter=blob:none --depth 1 https://github.com/gaaguirrer/Clases
git read-tree -mu HEAD
```

---

## Agregar carpeta nueva

```bash
# Agregar patrón a .git/info/sparse-checkout
git read-tree -mu HEAD
```

### Automatizado (PowerShell) — modo sincronización
Usar `git-automatizar.ps1` sin pensar en nombres:

```powershell
# Sincroniza: detecta carpetas nuevas en PC y las sube,
# también quita del sparse-checkout las que ya no existen.
.\git-automatizar.ps1 -Sincronizar

# Para correr sin preguntar confirmación:
.\git-automatizar.ps1 -Sincronizar -Forzar
```

## Quitar carpeta de mi PC (sin borrarla de GitHub)

```bash
# Quitar la línea de .git/info/sparse-checkout
git read-tree -mu HEAD
Remove-Item -Recurse -Force carpeta
```

## Actualizar todo

```bash
git pull
```

---

## Carpetas descargadas actualmente

- Administración de Sistemas de Información
- Gerencia de Operaciones I
- Sistemas electrónicos
- Ingeniería del Software I
- Libre I (SPSS)
- Marketing Digital
- Diseño de Bases de Datos
- Ingeniería del software III
- Gestión de Proyectos Tecnológicos
- Optativa profesional II (gobernanza y Criptografía)
