# ZBLS Algorithm Database

<p align="center">
  <a href="README.md">简体中文</a> | <strong>English</strong>
</p>

An online algorithm database covering **305 ZBLS cases**, with case diagrams, multiple algorithm options, and real-solve usage annotations.

ZBLS (Zborowski–Bruchem Last Slot) is an algorithm set that solves the last F2L pair while orienting the last-layer edges. This site follows the 42-category classification used by [SpeedCubingTips.eu](https://www.speedcubingtips.eu/zbls-zborowski-bruchem-last-slot/) and includes 305 cases, with algorithms used in actual solves by solvers including Xuanyi Geng and Yunzhi Lian. The already-solved case C37-4 is excluded; all other cases retain their original identifiers.

The base classification and source algorithms come from [SpeedCubingTips.eu](https://www.speedcubingtips.eu/zbls-zborowski-bruchem-last-slot/). Solver usage annotations are compiled from solve reconstructions, including those on [reco.nz](https://reco.nz/). **A solver annotation indicates past use in an actual solve, not necessarily a current go-to algorithm. Unannotated source algorithms do not imply use by any particular solver.**

The content is provided for learning and reference purposes and will continue to be updated. **If you find an incorrect algorithm or any other issue, feedback and corrections are welcome.**

## Content

- **305 ZBLS cases**: each case includes a state diagram and its corresponding algorithms, with multiple options available for some cases. Both category and individual case diagrams follow the light or dark theme.
- **42 categories**: C1–C36 have 8 cases each; C37 has 3; C38, C41, and C42 have 2 each; C39 and C40 have 4 each.
- **Real-solve annotations**: each algorithm is labeled with the solvers who have used it; when multiple solvers use the same algorithm, their names are shown together (e.g. “Xuanyi Yunzhi”).
- **Default Pro Library**: browse the curated algorithms and solver annotations immediately.
- **Personal libraries**: choose which pro algorithms to display and add your own algorithms in the same library. Use `.zbls` files for backups or transfers.

## Usage

### Browsing and choosing a library

Click the language (文 / A) icon in the top bar to choose **简体中文 / English**. Your first visit follows your browser’s preferred language; a manual choice is remembered. English mode displays known solver labels in English (e.g. 耿 → Xuanyi, 连 → Yunzhi). Personal library names, notes, and the original text in mark input fields are unchanged.

Open the site to start browsing. Within a category, use the scrollable category bar at the top to switch between C1–C42. Filter by **All / Learned / Unlearned**, or click the site logo in the upper-left corner to return home. Use the theme icon to switch between light and dark mode.

Click the question-mark icon to open **About this site**. The lower-right corner shows the site's latest publication time (UTC+8), covering algorithm, interface, and feature updates. Personal library edits and visits do not change this time.

The upper-right button shows the current library name. Click it to open library management:

- **Default Pro Library**: preview only; no personal library is needed to browse. Your first attempt to make a change prompts you to create your own library.
- **Personal libraries**: use the new-library button to create one with all pro algorithms initially visible. Each library lets you choose pro algorithms, add your own, and save images, notes, and learned status. Libraries keep their content and settings independently.
- **Managing libraries**: click a library name to switch to it. Use the menu beside a personal library to rename, export, or delete it.

When updated pro algorithms are published, reload the site to sync them into all personal libraries. Older `.zbls` imports are synced too. Existing show/hide choices are preserved; newly added pro algorithms are shown by default. Changes to solver annotations retain the corresponding algorithm's visibility choice. Your personal algorithms, notes, images, learned status, and case order stay unchanged. Importing an older file does not restore the retired, already-solved case C37-4.

### Editing and learning

A leading cube rotation (y, y′, or y2) appears as a separate small badge. U, U′, and U2 remain part of the algorithm text and do not receive a pre-AUF badge. This is display-only; the original algorithm text is unchanged.

In a personal library, click **Edit** on a case card:

- **Pro algorithms**: check or uncheck individual algorithms to show or hide them, or use **Select all / Select none** for that case. The original algorithms and solver annotations cannot be edited. Hiding an algorithm does not delete it.
- **My algorithms**: click **＋ Add**, enter the algorithm on the left, and optionally enter marks on the right, separated by spaces. You can edit these algorithms at any time. **Delete** removes the entire personal algorithm entry, including its marks.
- **Images and notes**: replace, clear, or restore an image, and add notes. Notes support multiple lines while editing; when browsing, they appear on one line with an ellipsis for overflow.
- **Save / Cancel**: click **Save** to keep your edits, or **Cancel** to discard them.

Use the round check button at the lower-right of a card to toggle learned status. Drag the handle at the upper-right to reorder cases without changing their identifiers (for example, C31-2 always remains C31-2). You can also click one algorithm per case to keep it highlighted; click it again to clear the selection. Selecting an algorithm does not change its order.

Learning progress in a website personal library is stored independently in the current browser and does not sync with the local database's learning progress.

### Backups and transfers

Click **Save** after editing, then export a `.zbls` file from the personal library's menu. The file includes your algorithms and marks, each case's pro-algorithm visibility settings, images, notes, learned status, ordering, and algorithm selections.

On another browser or device, open library management and choose **Import .zbls** to restore the file as a separate personal library.

**Personal libraries are stored in the current browser and do not sync automatically across devices. Clearing browser data may erase them, so export backups regularly.**

> Online: [https://cyrickyarar.github.io/zbls_site_static/](https://cyrickyarar.github.io/zbls_site_static/)
